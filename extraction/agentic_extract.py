from __future__ import annotations

try:
    from batch_processing.agentic_extract_app import main
except ImportError:  # pragma: no cover - allows direct script execution
    from agentic_extract_app import main  # type: ignore


if __name__ == "__main__":
    main()
