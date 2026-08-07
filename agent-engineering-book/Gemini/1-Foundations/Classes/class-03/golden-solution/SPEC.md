# WidgetWare SDR Lab — Specification

This document defines required behavior, prohibited behavior, and completion criteria for the system. It is technology-aware (Gemini, ADK, Antigravity) but not technology-dependent — it states what must be true, not which class must implement it.

## Business objective

Help a WidgetWare SDR decide, quickly and defensibly, whether a target company is worth pursuing, and produce a first-draft outreach message grounded in real evidence — without ever sending anything without a human's explicit approval.

## Required behavior

- Accept a target company (by name, domain, or an existing internal account record).
- Retrieve any approved account information WidgetWare already holds for that company.
- Research permitted public evidence about the company relevant to fit and timing.
- Evaluate the company against WidgetWare's configured ideal-customer profile (ICP).
- Produce a structured, machine-validated qualification result — not free-form prose.
- When qualification succeeds, draft an outreach message using only approved, evidence-backed facts.
- Present a human with the qualification, the supporting evidence, and the draft, and require an explicit approve / reject / revise decision before anything else happens.
- Explain its qualification decision in a way a person can audit — which criteria matched, which evidence supported them, what is still unknown.

## Prohibited behavior

- Sending an email, social message, or any other outbound communication autonomously.
- Modifying a CRM record without a prior human approval.
- Inventing a company attribute, contact, or fact not present in supplied or retrieved evidence.
- Scraping or querying sources outside an approved list.
- Bypassing authentication or source access restrictions.
- Making legal, contractual, or pricing commitments on WidgetWare's behalf.
- Treating an inference or a model's self-reported confidence as if it were a verified fact.

## Inputs and outputs

- **Input:** a target company identifier, plus whatever internal account context already exists.
- **Output:** a structured qualification result, an evidence-backed outreach draft (when qualification succeeds), and a request for human approval.

## State transitions

Defined in full starting in Class 8 (Book 1, Chapter 9). At this checkpoint, only the terminal boundary matters: no state this system can reach permits an autonomous send.

## Error behavior

When evidence is insufficient to qualify a company one way or the other, the system must say so explicitly (`NEEDS_RESEARCH`) rather than guess. When something fails outright (a malformed result, an unavailable dependency), the system must fail to a visible, named state (`BLOCKED`), never to a silently wrong answer.

## Approval rules

No outbound action of any kind may occur without a prior, explicit, human-approved state. This is a structural guarantee, not an instruction the model is asked to follow — Book 1 contains no send-capable tool anywhere in the codebase, by design, through Chapter 11.

## Completion criteria for this checkpoint (Class 1)

- [x] Business objective is stated in one sentence a stakeholder could repeat back correctly.
- [x] Required and prohibited behavior are both explicit and reviewable.
- [x] Every acceptance criterion in `docs/acceptance-criteria.md` is independently testable.
- [x] No agent code exists yet — this chapter is charter only.
