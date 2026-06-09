"""
Embedding-based similarity for DVs_Definitions comparison.

Primary: OpenAI text-embedding-3-small with a file-based cache
         (so subsequent evaluation runs are instant).
Fallback: word-vector cosine similarity (numpy) when no OPENAI_API_KEY is set.
"""
from __future__ import annotations

import hashlib
import json
import os
import re
from pathlib import Path


def _load_dotenv() -> None:
    """Load .env from the project root into os.environ if OPENAI_API_KEY is missing."""
    if os.getenv("OPENAI_API_KEY"):
        return
    env_path = Path(__file__).resolve().parent.parent / ".env"
    if not env_path.exists():
        return
    for raw_line in env_path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, _, value = line.partition("=")
        os.environ.setdefault(key.strip(), value.strip())


_load_dotenv()

EMBEDDING_CACHE_PATH: Path = Path(__file__).resolve().parent / "embedding_cache.json"
EMBEDDING_MODEL = "text-embedding-3-small"


def _load_cache() -> dict[str, list[float]]:
    if EMBEDDING_CACHE_PATH.exists():
        try:
            return json.loads(EMBEDDING_CACHE_PATH.read_text(encoding="utf-8"))
        except Exception:
            pass
    return {}


def _save_cache(cache: dict[str, list[float]]) -> None:
    EMBEDDING_CACHE_PATH.write_text(
        json.dumps(cache, ensure_ascii=False, separators=(",", ":")),
        encoding="utf-8",
    )


def _text_key(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()[:24]


def _get_embeddings_openai(texts: list[str]) -> list[list[float]] | None:
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        return None
    try:
        from openai import OpenAI

        client = OpenAI(api_key=api_key)
        cache = _load_cache()

        keys = [_text_key(t) for t in texts]
        missing_texts = [t for t, k in zip(texts, keys) if k not in cache]

        if missing_texts:
            response = client.embeddings.create(model=EMBEDDING_MODEL, input=missing_texts)
            for text, item in zip(missing_texts, response.data):
                cache[_text_key(text)] = item.embedding
            _save_cache(cache)

        return [cache[k] for k in keys]
    except Exception:
        return None


_STOPWORDS = frozenset(
    "a an the of in for and or to at by from with on is are was were be been being "
    "per as its their this that each any some".split()
)


def _word_tokens(text: str) -> list[str]:
    return [w for w in re.split(r"[\s_\-/,;.()\[\]]+", text.lower()) if w and w not in _STOPWORDS]


def _word_vector_cosine_matrix(texts_a: list[str], texts_b: list[str]) -> list[list[float]]:
    """Word-count cosine similarity matrix using numpy. No external dependencies."""
    try:
        import numpy as np
    except ImportError:
        n, m = len(texts_a), len(texts_b)
        return [[0.0] * m for _ in range(n)]

    vocab: dict[str, int] = {}
    all_texts = texts_a + texts_b
    for text in all_texts:
        for w in _word_tokens(text):
            if w not in vocab:
                vocab[w] = len(vocab)

    if not vocab:
        n, m = len(texts_a), len(texts_b)
        return [[0.0] * m for _ in range(n)]

    def to_vec(text: str) -> "np.ndarray":
        v = np.zeros(len(vocab))
        for w in _word_tokens(text):
            if w in vocab:
                v[vocab[w]] += 1
        return v

    vecs = np.array([to_vec(t) for t in all_texts], dtype=float)
    norms = np.linalg.norm(vecs, axis=1, keepdims=True)
    norms = np.where(norms < 1e-9, 1.0, norms)
    vecs_norm = vecs / norms
    a_vecs = vecs_norm[: len(texts_a)]
    b_vecs = vecs_norm[len(texts_a) :]
    return (a_vecs @ b_vecs.T).tolist()


def similarity_matrix(texts_a: list[str], texts_b: list[str]) -> list[list[float]]:
    """
    Return a matrix[i][j] = cosine_similarity(texts_a[i], texts_b[j]).
    Uses OpenAI embeddings when OPENAI_API_KEY is set, otherwise TF-IDF.
    """
    if not texts_a or not texts_b:
        return []

    all_texts = texts_a + texts_b
    embeddings = _get_embeddings_openai(all_texts)

    if embeddings is not None:
        import numpy as np

        emb = np.array(embeddings, dtype=float)
        norms = np.linalg.norm(emb, axis=1, keepdims=True)
        norms = np.where(norms < 1e-9, 1.0, norms)
        emb_norm = emb / norms
        a = emb_norm[: len(texts_a)]
        b = emb_norm[len(texts_a) :]
        return (a @ b.T).tolist()

    return _word_vector_cosine_matrix(texts_a, texts_b)


def soft_f1(
    h_defs: list[str],
    l_defs: list[str],
    threshold: float = 0.70,
) -> float:
    """
    Soft F1 between two definition lists using embedding cosine similarity.

    For each human definition, the best-matching LLM definition is found.
    A match is counted if the similarity >= threshold.
    Precision and recall are averaged into an F1 score.
    """
    if not h_defs and not l_defs:
        return 1.0
    if not h_defs or not l_defs:
        return 0.0

    mat = similarity_matrix(h_defs, l_defs)
    if not mat:
        return 0.0

    h_matched = sum(1 for row in mat if max(row, default=0.0) >= threshold)
    l_matched = sum(
        1
        for j in range(len(l_defs))
        if max((mat[i][j] for i in range(len(h_defs))), default=0.0) >= threshold
    )

    recall = h_matched / len(h_defs)
    precision = l_matched / len(l_defs)
    if precision + recall == 0:
        return 0.0
    return 2 * precision * recall / (precision + recall)
