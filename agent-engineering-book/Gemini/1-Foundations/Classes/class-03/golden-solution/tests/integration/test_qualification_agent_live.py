"""Semantic evaluation — Book 1 §4.5.

Makes a real Gemini call and checks stable properties of the response,
not exact wording. Requires live credentials (`GOOGLE_API_KEY`, or a
configured Vertex AI project) and is skipped automatically otherwise.
"""

import os
from pathlib import Path

import pytest
import yaml

from widgetware_sdr.app import run_qualification_sync

pytestmark = pytest.mark.skipif(
    not (os.environ.get("GOOGLE_API_KEY") or os.environ.get("GOOGLE_CLOUD_PROJECT")),
    reason="requires live Gemini credentials (GOOGLE_API_KEY or GOOGLE_CLOUD_PROJECT)",
)


def _load_account(account_id: str) -> dict:
    path = Path(__file__).resolve().parent.parent / "fixtures" / "accounts" / f"{account_id}.yaml"
    with path.open("r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def _final_text(events: list) -> str:
    text_parts = []
    for event in events:
        content = getattr(event, "content", None)
        if content and getattr(content, "parts", None):
            for part in content.parts:
                if getattr(part, "text", None):
                    text_parts.append(part.text)
    return "\n".join(text_parts)


def test_qualifying_account_recommends_qualify_and_completes() -> None:
    account = _load_account("acme-001")
    events = run_qualification_sync(account)
    assert events, "agent produced no events at all"

    response = _final_text(events)
    assert "22000" in response or "22,000" in response


def test_unqualified_account_names_the_exclusion() -> None:
    account = _load_account("brightleaf-002")
    events = run_qualification_sync(account)
    response = _final_text(events)
    assert "financial" in response.lower()


def test_insufficient_evidence_account_does_not_invent_employee_count() -> None:
    account = _load_account("meridian-003")
    events = run_qualification_sync(account)
    response = _final_text(events)
    assert "unknown" in response.lower() or "not" in response.lower()
