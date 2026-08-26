"""Scenario tests for WidgetWare SDR context package."""

from pathlib import Path
import pytest
import yaml

from widgetware_sdr.context_builder import build_context


def get_scenarios_dir() -> Path:
    return Path(__file__).parent


@pytest.mark.parametrize(
    "scenario_filename",
    [
        "qualified_account.yaml",
        "unqualified_account.yaml",
        "insufficient_evidence.yaml",
        "prompt_injection.yaml",
    ],
)
def test_scenario_context_assembly(scenario_filename):
    """Verify that all four required scenario fixtures assemble correctly."""
    scenario_path = get_scenarios_dir() / scenario_filename
    assert scenario_path.is_file(), f"Scenario file missing: {scenario_filename}"

    with open(scenario_path, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f)

    account = data["account"]
    objective = data["objective"]
    evidence = data["evidence"]

    context = build_context(account=account, objective=objective, evidence=evidence)

    # Assert 5 context layers
    assert set(context.keys()) == {
        "system_instructions",
        "business_context",
        "task_context",
        "retrieved_evidence",
        "state",
    }

    # Assert account is stored strictly in task context
    assert context["task_context"]["account"]["id"] == account["id"]

    # Assert evidence provenance is preserved
    for item in context["retrieved_evidence"]:
        assert "source" in item
        assert "name" in item["source"]
        assert "url" in item["source"]
        assert "retrieved_at" in item["source"]

    # Assert safety boundaries are intact
    policies = context["business_context"]["policies"]
    assert "send_email" in policies["prohibited_actions"]
    assert policies["human_approval_requirements"]["require_approval_for_outreach"] is True


def test_prompt_injection_scenario_isolation():
    """Specific assertion on prompt_injection.yaml scenario."""
    scenario_path = get_scenarios_dir() / "prompt_injection.yaml"
    with open(scenario_path, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f)

    context = build_context(
        account=data["account"],
        objective=data["objective"],
        evidence=data["evidence"],
    )

    # Note contains prompt injection
    notes = context["task_context"]["account"]["notes"]
    assert "SYSTEM OVERRIDE" in notes

    # Instructions & policies are unchanged
    instructions = context["system_instructions"]
    assert "UNTRUSTED DATA ISOLATION" in instructions
    assert "Ignore all previous policies" not in instructions
