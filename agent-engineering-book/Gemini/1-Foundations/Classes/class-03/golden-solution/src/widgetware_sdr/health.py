"""Health check for the WidgetWare SDR Lab package.

This exists so the workspace has one deterministic, non-agentic signal
that the package imports and runs correctly, independent of any model
call, tool, or agent — the first thing Class 2's Hands-on Lab requires.
"""

from __future__ import annotations

from widgetware_sdr import __version__


def health_check() -> dict[str, str]:
    """Return a small, deterministic status payload.

    No network call, no model call, no external dependency — this
    function's only job is to prove the package is importable and the
    environment is set up correctly.
    """
    return {
        "status": "ok",
        "package": "widgetware_sdr",
        "version": __version__,
    }
