# WidgetWare SDR Context Package — Class 03

## Overview
This repository contains the structured, testable **Context Package** for the WidgetWare SDR system. It defines the business configuration, operating policies, stable agent instructions, and context assembly logic required before building an AI agent in Class 4.

## Five Context Layers
The context package enforces strict separation of five context layers to guarantee that untrusted input (such as account notes or retrieved web text) cannot override core business policies or system instructions:

1. **System Instructions (`system_instructions`):** Stable behavioral rules, operating boundaries, uncertainty handling, and human escalation policies defined in `src/widgetware_sdr/instructions.py`.
2. **Business Context (`business_context`):** Canonical business data loaded from YAML:
   - `config/products.yaml`: Products, target buyers, approved/prohibited claims.
   - `config/icp.yaml`: Ideal Customer Profile, fit dimensions, employee thresholds (min 500).
   - `config/policies.yaml`: Evidence classifications, prohibited actions, human approval rules.
3. **Task Context (`task_context`):** Current assignment data including `account` details and `objective`. Account notes live here as untrusted data.
4. **Retrieved Evidence (`retrieved_evidence`):** Evidence records with full provenance (`name`, `url`, `retrieved_at`).
5. **Workflow State (`state`):** Execution state dictionary (defaults to `{}`).

## Project Structure
```text
my-work/class-03/
├── README.md
├── SPEC.md
├── LAB.md
├── pyproject.toml
├── .env.example
├── config/
│   ├── products.yaml
│   ├── icp.yaml
│   └── policies.yaml
├── docs/
│   ├── widgetware-business-brief.md
│   └── acceptance-criteria.md
├── src/
│   └── widgetware_sdr/
│       ├── __init__.py
│       ├── instructions.py
│       └── context_builder.py
└── tests/
    ├── unit/
    │   └── test_context_builder.py
    └── scenarios/
        ├── qualified_account.yaml
        ├── unqualified_account.yaml
        ├── insufficient_evidence.yaml
        ├── prompt_injection.yaml
        └── test_scenarios.py
```

## Setup & Testing Instructions

### 1. Environment Setup
```bash
# In my-work/class-03 directory:
uv venv .venv
source .venv/bin/activate
uv pip install -e ".[dev]"
```

### 2. Run Tests
```bash
.venv/bin/pytest -v
```

## Safety Boundaries
- **No ADK Agent or LLM Calls:** Pure deterministic Python context assembly.
- **No Side Effects:** Prohibits outreach, CRM edits, and pricing commitments without explicit human approval.
- **Prompt Injection Defense:** Account notes are treated as untrusted data and cannot alter instructions or policies.
