from __future__ import annotations

"""Compatibility entrypoint for the hybrid extraction CLI."""

try:
    from batch_processing.hybrid_extract_app import main
except ImportError:  # pragma: no cover - allows direct script execution
    from hybrid_extract_app import main  # type: ignore


if __name__ == "__main__":
    main()
