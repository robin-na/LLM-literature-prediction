from __future__ import annotations

"""Primary entrypoint for paper extraction workflows."""

try:
    from batch_processing.extract_papers_app import main
except ImportError:  # pragma: no cover - allows direct script execution
    from extract_papers_app import main  # type: ignore


if __name__ == "__main__":
    main()
