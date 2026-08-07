"""Deterministic, offline tests for agent construction.

None of these require a live Gemini call — they check the structural
contract (Book 1 §4's Evaluation checklist: "are model and instructions
loaded from centralized configuration?"), not whether the agent
reasons well. Semantic evaluation lives in tests/integration/, and
requires live credentials.
"""

from widgetware_sdr.agents.qualification_agent import (
    build_agent_instruction,
    create_qualification_agent,
)
from widgetware_sdr.instructions import DEFAULT_MODEL_ID


def test_agent_has_a_name_and_the_centrally_configured_model() -> None:
    agent = create_qualification_agent()
    assert agent.name == "qualification_agent"
    assert agent.model == DEFAULT_MODEL_ID


def test_agent_description_does_not_claim_prohibited_capabilities() -> None:
    agent = create_qualification_agent()
    description = agent.description.lower()
    for prohibited in ("send", "email", "crm"):
        assert prohibited not in description


def test_instruction_includes_the_real_icp_thresholds_not_hardcoded_copies() -> None:
    instruction = build_agent_instruction()
    assert "5000" in instruction
    assert "manufacturing" in instruction
    assert "financial_services" in instruction


def test_instruction_includes_the_embedded_qualification_procedure() -> None:
    """This checkpoint deliberately embeds the procedure directly in the
    agent's instruction — Chapter 5 is where it gets extracted into a
    Skill, not here.
    """
    instruction = build_agent_instruction()
    assert "Check explicit exclusion criteria first" in instruction
    assert "QUALIFY" in instruction
    assert "DO_NOT_QUALIFY" in instruction
    assert "NEEDS_RESEARCH" in instruction


def test_instruction_contains_no_specific_account_data() -> None:
    """The static instruction must never be built per-account — that's
    the task context's job (see app.py's render_task_message), kept
    separate per Book 1 §3.2.
    """
    instruction = build_agent_instruction()
    assert "Acme Manufacturing" not in instruction
    assert "acme-001" not in instruction
    assert "22000" not in instruction


def test_agent_has_no_tools() -> None:
    """Book 1 §4.2: this agent may not call external services. Tools
    arrive in Chapter 7, several classes from now.
    """
    agent = create_qualification_agent()
    assert not getattr(agent, "tools", [])


def test_no_skills_directory_exists_yet() -> None:
    """A structural check for this checkpoint's own honesty: Chapter 5
    is what introduces skills/ — it should not exist here."""
    from pathlib import Path

    repo_root = Path(__file__).resolve().parent.parent.parent
    assert not (repo_root / "skills").exists()
