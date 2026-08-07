# Acceptance Criteria — Class 3 WidgetWare SDR Context Package

## Context Layer Isolation
- [x] Context builder returns 5 distinct top-level keys: `system_instructions`, `business_context`, `task_context`, `retrieved_evidence`, `state`.
- [x] Account notes and task input appear only in `task_context`.
- [x] Prompt injection in task notes cannot alter `system_instructions` or `business_context.policies`.

## Configuration Loading
- [x] Loads `products.yaml`, `icp.yaml`, and `policies.yaml` deterministically from `config/`.
- [x] Raises explicit `FileNotFoundError` or `ValueError` if required configuration files or sections are missing.

## Evidence Provenance & Classification
- [x] Every evidence record retains provenance (`name`, `url`, `retrieved_at`).
- [x] Allowed classifications: `verified_fact`, `derived_fact`, `inference`, `unknown`, `conflict`.

## Safety & Boundaries
- [x] Prohibits unapproved outreach, CRM modification, and contract commitments.
- [x] Missing account information remains explicitly missing (`unknown`) rather than fabricated.
- [x] Input dictionary parameters are not mutated during context assembly.
