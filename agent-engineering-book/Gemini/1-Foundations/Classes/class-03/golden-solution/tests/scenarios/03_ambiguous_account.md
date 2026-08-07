# Scenario: Ambiguous account

**Company:** Meridian Industrial Group
**Industry:** Industrial automation (self-described; not independently confirmed)
**Employee count:** Unknown — company is privately held and does not publish headcount
**Region:** Europe
**Known signal:** A recent press mention of "modernization initiatives," with no further detail.

## Expected qualification direction

`NEEDS_RESEARCH` — industry and region are plausible fits, but employee count cannot be confirmed and the modernization signal is too vague to count as a decisive pain signal on its own.

## What the system must be able to explain

Exactly which piece of information is missing (confirmed employee count) and why the existing signal is insufficient on its own to qualify or disqualify the account — and that the system did not guess a plausible-sounding employee count to resolve the ambiguity.

## Structured versions

- Input: [`../fixtures/accounts/meridian-003.yaml`](../fixtures/accounts/meridian-003.yaml)
- Expected output: [`../fixtures/expected/meridian-003.yaml`](../fixtures/expected/meridian-003.yaml)
