# Scenario: Disqualifying account

**Company:** Bright Leaf Financial Advisors
**Industry:** Financial services
**Employee count:** 300
**Region:** United States
**Known signal:** None relevant to plant modernization or industrial automation.

## Expected qualification direction

`NOT_QUALIFIED` — fails on industry (not manufacturing or industrial automation) and on employee count (below the 5,000 minimum).

## What the system must be able to explain

Which specific ICP exclusion(s) were triggered — industry, size, or both — stated plainly enough that an SDR would not need to ask why.

## Structured versions

- Input: [`../fixtures/accounts/brightleaf-002.yaml`](../fixtures/accounts/brightleaf-002.yaml)
- Expected output: [`../fixtures/expected/brightleaf-002.yaml`](../fixtures/expected/brightleaf-002.yaml)
