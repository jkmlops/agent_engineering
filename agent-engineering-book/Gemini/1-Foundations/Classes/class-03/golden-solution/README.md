# WidgetWare SDR Lab

A bounded agent system that researches, qualifies, and drafts outreach to prospective manufacturing and industrial-automation accounts on WidgetWare's behalf — and stops for human approval before anything leaves the building.

This checkpoint (Class 3 / `golden-solutions/class-03/`) adds the first working ADK agent and its first real Gemini model call. The qualification procedure is embedded directly in the agent's instruction as a plain string — Chapter 5 is where this gets extracted into a reusable Skill, deliberately not done here yet.

## Quick start

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
cp .env.example .env  # fill in GOOGLE_API_KEY (or GOOGLE_CLOUD_PROJECT) to run the agent for real
./scripts/check.sh    # runs format check, lint, and tests — live-model tests skip automatically without credentials
```

## What's new this class

- `src/widgetware_sdr/agents/qualification_agent.py` — the Account Qualification Assistant: a real `google.adk.agents.Agent`, its instruction assembled from fixed system instructions + business config + an embedded qualification procedure (a plain string constant, not yet a Skill)
- `src/widgetware_sdr/app.py` — the local run harness: `Runner` + `InMemorySessionService`, renders the account and evidence as the per-call user message
- `data/sample_accounts/` — the three scenario accounts, as the book's own Hands-on Lab structure expects (see `KNOWN_FAILURE_CASES.md` #2 for how this relates to `tests/fixtures/`)
- `tests/unit/` — offline, deterministic tests: agent construction, instruction content (including a check that no `skills/` directory exists yet), message rendering
- `tests/integration/test_qualification_agent_live.py` — 3 semantic evaluation tests that make a real Gemini call; skip automatically without credentials

## Repository structure

```text
widgetware-sdr/
├── README.md / SPEC.md / pyproject.toml / .env.example
├── docs/
├── config/
├── data/sample_accounts/
├── src/widgetware_sdr/
│   ├── instructions.py
│   ├── context_builder.py
│   ├── app.py
│   └── agents/qualification_agent.py   # procedure embedded here, no skills/ yet
├── tests/
│   ├── unit/
│   ├── integration/     # requires live credentials; skips otherwise
│   ├── contracts/        # populated starting Class 5
│   ├── scenarios/
│   └── fixtures/
└── scripts/check.sh
```

## Running the agent for real

Requires `GOOGLE_API_KEY` (or a configured Vertex AI project) in your environment:

```python
from widgetware_sdr.app import run_qualification_sync
import yaml

with open("data/sample_accounts/acme-001.yaml") as f:
    account = yaml.safe_load(f)

events = run_qualification_sync(account)
for event in events:
    print(event)
```

Without credentials, agent *construction* still works — only actually running it requires a live call.

## Known failure cases

See [`KNOWN_FAILURE_CASES.md`](KNOWN_FAILURE_CASES.md) — in particular #1: a clean test run in this environment proves construction, not reasoning quality.

## Completion checklist

Before treating this checkpoint as done:

- [ ] `build_agent_instruction()` contains the real ICP thresholds (read from config) and the embedded qualification procedure — not a hardcoded restatement of the config values.
- [ ] The agent's static instruction contains no specific account data anywhere.
- [ ] The agent has no tools attached — tools arrive in Class 6.
- [ ] No `skills/` directory exists yet — that's Class 4's deliverable, not this one's.
- [ ] `./scripts/check.sh` passes with the live-model tests reporting **skipped**, not failed, when no credentials are set.

## Starting Class 4

1. Start from this checkpoint. Class 4 does not touch `app.py` or the agent's boundary — it extracts the qualification procedure out of `qualification_agent.py`'s embedded string and into `skills/icp_qualification/skill.md`, then updates the agent to load it instead.
2. Everything this checkpoint's tests verify about the agent's construction should still hold after Class 4 — only *where* the procedure text lives changes.
3. See `../../class-04/` for what Class 4 adds.

## Status

- [x] Class 1 — Project charter, and the Antigravity workspace and repository harness
- [x] Class 2 — Gemini context and instruction architecture
- [x] Class 3 — First ADK agent (embedded procedure)
- [ ] Classes 4–10 — see `../../00_Course_Framework.md`
