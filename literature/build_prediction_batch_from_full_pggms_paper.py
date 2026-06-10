from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from prediction_inputs.paper_only_variants import (  # noqa: E402
    MODEL_TAGS,
    build_joint_prompt,
    build_joint_system_prompt,
    build_openai_request,
)


DEFAULT_MODELS = [
    "gpt-4.1-2025-04-14",
    "gpt-4.1-mini-2025-04-14",
    "gpt-4.1-nano-2025-04-14",
    "gpt-5.1",
    "gpt-5-mini",
    "gpt-5-nano",
]
DEFAULT_PAPER_PATH = Path("paper_collection/papers_markdown_cleaned/PGG_MS_202502.md")

FULL_PAPER_WRAPPER = """Below is the full text of one academic paper.
Use it as contextual evidence about how design features may change the efficiency impact of peer punishment.
Use only claims supported by the paper text, and do not infer beyond what the paper supports."""


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Build joint-with-explanation prediction batch JSONLs that augment the "
            "validation task with the full cleaned PGG_MS manuscript text."
        )
    )
    parser.add_argument(
        "--df-pgg",
        type=Path,
        default=Path("input/pgg_CONFIGmerged_validation.csv"),
        help="Validation configurations to predict.",
    )
    parser.add_argument(
        "--paper-path",
        type=Path,
        default=DEFAULT_PAPER_PATH,
        help="Cleaned markdown paper path for the full-text benchmark paper.",
    )
    parser.add_argument(
        "--paper-id",
        default="PGG_MS_202502",
        help="Identifier to use in the custom_id suffix.",
    )
    parser.add_argument(
        "--models",
        nargs="+",
        default=DEFAULT_MODELS,
        help="Model names to generate batch files for.",
    )
    parser.add_argument(
        "--n-repeats",
        type=int,
        default=5,
        help="Number of repeated calls per model.",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path("openAI_batch_input"),
        help="Directory for output JSONL files.",
    )
    parser.add_argument(
        "--output-prefix",
        default="prediction_literature_fullpaper_pggms_joint_reps1to5",
        help="Prefix for output JSONL filenames.",
    )
    return parser.parse_args()


def _model_tag(model: str) -> str:
    return MODEL_TAGS.get(model, "".join(ch for ch in model.lower() if ch.isalnum()))


def _wrap_full_paper(paper_text: str, prompt_text: str) -> str:
    return (
        f"{FULL_PAPER_WRAPPER}\n"
        "----------Paper Starts----------\n\n"
        f"{paper_text.strip()}\n\n"
        "----------Paper Ends----------\n"
        f"{prompt_text}"
    )


def _sanitize_paper_text(text: str) -> str:
    # Keep the visible citation/reference text but strip Paperpile link targets.
    text = re.sub(r"\[([^\]]+)\]\((?:https?://)?paperpile\.com[^)]*\)", r"\1", text)
    text = re.sub(r"(?:https?://)?paperpile\.com/\S+", "", text)
    # Drop the trailing bibliography so the prompt stays focused on the paper body.
    text = re.sub(r"\nReferences\s*\n.*\Z", "\n", text, flags=re.IGNORECASE | re.DOTALL)
    return text


def _build_requests(
    *,
    df: pd.DataFrame,
    model: str,
    n_repeats: int,
    paper_id: str,
    paper_text: str,
) -> list[dict]:
    requests: list[dict] = []
    for rep_idx in range(1, n_repeats + 1):
        requests.append(
            build_openai_request(
                custom_id=f"paper_full_text_joint_rep{rep_idx}/{paper_id}",
                model=model,
                system_prompt=build_joint_system_prompt(include_explanation=True),
                user_prompt=_wrap_full_paper(
                    paper_text,
                    build_joint_prompt(df, include_explanation=True),
                ),
                include_logprobs=False,
                response_format_json=True,
                include_explanation=True,
            )
        )
    return requests


def _write_jsonl(path: Path, records: list[dict]) -> int:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as handle:
        for record in records:
            handle.write(json.dumps(record, ensure_ascii=False) + "\n")
    return len(records)


def main() -> None:
    args = parse_args()
    df = pd.read_csv(args.df_pgg).sort_values("CONFIG_configId").reset_index(drop=True)
    paper_text = _sanitize_paper_text(args.paper_path.read_text(encoding="utf-8"))

    for model in args.models:
        requests = _build_requests(
            df=df,
            model=model,
            n_repeats=args.n_repeats,
            paper_id=args.paper_id,
            paper_text=paper_text,
        )
        output_path = args.output_dir / f"{args.output_prefix}_{_model_tag(model)}.jsonl"
        count = _write_jsonl(output_path, requests)
        print(f"Wrote {count} requests to {output_path}")


if __name__ == "__main__":
    main()
