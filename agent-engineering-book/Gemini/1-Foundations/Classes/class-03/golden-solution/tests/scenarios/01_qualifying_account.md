# Scenario: Qualifying account

**Company:** Acme Manufacturing
**Industry:** Manufacturing
**Employee count:** 22,000
**Region:** United States
**Known signal:** Legacy plant-floor systems with no path to AI-enabled automation; operations team still runs approvals through paper checklists.

## Expected qualification direction

`QUALIFIED` — meets the industry, size, and region criteria, and shows a concrete pain signal matching WidgetWare's ICP.

## What the system must be able to explain

Which specific ICP criteria matched (industry, employee count, region), and which specific evidence item supports the pain signal.

## Structured versions

- Input: [`../fixtures/accounts/acme-001.yaml`](../fixtures/accounts/acme-001.yaml)
- Expected output: [`../fixtures/expected/acme-001.yaml`](../fixtures/expected/acme-001.yaml)
