# Known Failure Cases — Class 3 Checkpoint

## Carried forward from Classes 1–2

- `expected_qualification_direction`/`rationale` in fixtures are still hand-derived predictions, unverified by any code.
- Business-config drift between `config/icp.yaml` and the fixture `expected/*.yaml` files is still undetected by any test.
- The three scenario accounts remain illustrative, not a representative dataset.

## New at this checkpoint

### 1. The three semantic scenario tests are skipped by default in this environment

`tests/integration/test_qualification_agent_live.py` requires `GOOGLE_API_KEY` or a configured Vertex AI project. Without one, `pytest` reports these as **skipped**, not passed — do not mistake a clean `18 passed, 3 skipped` run for proof the agent reasons correctly. The 18 passing tests only prove the agent *constructs* correctly (right model, right instruction content, no leaked account data, no tools). Whether it actually avoids inventing an employee count or correctly explains a `NEEDS_RESEARCH` outcome is unverified until someone runs the integration suite with real credentials.

### 2. `data/sample_accounts/` and `tests/fixtures/accounts/` are duplicated, not shared

Book 1 §4's Hands-on Lab asks for sample account profiles under `data/sample_accounts/`, and this checkpoint already had `tests/fixtures/accounts/` from Class 2. Rather than pick one, this checkpoint keeps both, with identical content, for two different audiences. They are not read from a single source — if one is edited without the other, they will silently drift.

### 3. The qualification procedure is embedded directly in this file, by design — and that's the whole point of this checkpoint

`EMBEDDED_QUALIFICATION_PROCEDURE` in `qualification_agent.py` is a plain string constant. This is not a mistake to fix — it is the honest "before" state Class 4's Skill extraction is measured against. If you're comparing this checkpoint to a later one and wondering why the procedure "duplicates" what's in `skills/icp_qualification/skill.md` in Class 4, it's because Class 4 is precisely the class that moves it there.

### 4. The agent's prose output format is not yet validated

Nothing in this checkpoint checks that the model's response actually uses one of `QUALIFY` / `DO_NOT_QUALIFY` / `NEEDS_RESEARCH`, or in what format. That gap is closed in Class 5 (structured outputs) — this checkpoint's output is still free-form prose, exactly as intended.
