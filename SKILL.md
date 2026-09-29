---
name: research-pipeline
description: "Design and advance computational research from existing data to executable analyses and verifiable results. Use for research questions, study or experiment design, scientific feasibility, bioinformatics pipelines, model evaluation, and research-pipeline repair. 科研设计、研究方向、实验设计、科学可行性、搭建或修复分析流程。Do not use for a standalone factual lookup, translation, or prose-only edit."
license: MIT
metadata:
  version: "0.1.1"
---

# Research Pipeline

Turn the user's current research objective into a completed, reviewable stage with evidence proportionate to its claims. Reuse the project's existing code, contracts, data and specialist tools.

## Choose the work, not a larger workflow

Infer the requested mode from the current task. Combine modes only where needed.

- **Design:** turn available resources into a testable question and a feasible measurement or experiment. Read [design.md](references/design.md).
- **Implement or repair:** deliver working code, real tool calls and appropriate verification. Read [execution.md](references/execution.md).
- **Evaluate:** assess identity, independence, leakage, comparisons and claims. Read [evidence.md](references/evidence.md).
- **Resume or hand off:** recover decisions, changes of scope and outstanding dependencies. Read [state.md](references/state.md).

Read only the relevant references. A design request does not authorize executing experiments; an implementation request must not end at a proposal when the authorized work can be completed. A small task does not require a new planning system.

## Establish the current contract

Inspect only the authoritative instructions, inputs and evidence needed for the current stage. Inspect code/worktree and execution receipts when this task depends on implementation or prior runs; reuse records that remain valid. Refresh facts that affect this stage.

Identify:
- the research object, target state, observable measurements and existing evidence;
- the user's current objective, success criteria, resource limits and authorized actions;
- the current stage's inputs, deliverables and explicit stopping conditions.

Distinguish durable constraints from temporary stage restrictions. A later explicit authorization can replace an earlier stage restriction; it does not silently authorize unrelated publication, transfers or merges. Preserve the user's chosen scientific endpoint unless a change is explicitly accepted.

If information is missing, first inspect available sources. Use stated, reversible assumptions for routine choices. Ask only for information or decisions that materially change the work, while completing independent authorized tasks.

## Use an evidence-feedback loop

Apply engineering-control reasoning qualitatively: compare observed state with the target, select an action within the constraints, measure its effect, and correct the deviation.

Define how progress can be observed before a costly run. A short diagnostic should resolve a material uncertainty, not become a permanent substitute for the complete requested stage. Optimize measured reliability, cost, runtime or scientific information; explain tradeoffs when no optimum is established. Do not claim mathematical observability, controllability or stability without a specified model and analysis.

After repeated failures under the same hypothesis, revisit the object, inputs, environment and hypothesis. After three unsuccessful attempts, design a discriminating diagnostic instead of repeating the same fix. Stop earlier when evidence indicates a harmful or out-of-scope action.

## Keep three judgments separate

1. **Engineering:** what has been implemented, actually executed, recovered and verified?
2. **Science:** what can the measurements and evaluation support, and under which population, context and independence assumptions?
3. **Authorization:** which next actions are already allowed, and which require a new decision?

A working interface does not validate a biological claim. A hypothesis with insufficient labels does not automatically prohibit an authorized software component that does not depend on those labels. Attach a HOLD or failure to its actual dependency and continue the rest of the authorized stage.

When appropriate, recommend GO, REVISE or HOLD for a named next stage. State the evidence and what the verdict permits; do not silently turn this recommendation into authorization.

## Build evidence into the implementation

Use the repository's existing schemas, validators, tests and receipts. Add deterministic checks only where a new failure mode warrants them. Skill prose and model agreement cannot enforce a gate by themselves.

Preserve:
- the meaning of inputs and outputs, including units, context, missingness and native score semantics;
- source and transformation identities separately from statistical dependence and split groups;
- frozen confirmatory rules, with later changes recorded as new versions;
- original inputs, historical attempts and failed or unevaluable results;
- the distinction between an experiment specification and each execution attempt.

Never manufacture a prediction for an unfitted task, reinterpret missing as negative without justification, relax a rule to obtain a positive result, or treat repeated processing as new independent evidence.

## Deliver the whole authorized stage

Implement and run what can be executed. Verify the final code/configuration state that actually produced the results. If an input or method changes, invalidate and rerun the affected checks; do not mechanically repeat unrelated expensive work.

Report:
- the new usable capability or finding;
- what was verified, with the relevant artifacts or receipts;
- what remains uncertain or blocked and the exact dependency;
- a concrete request only when user input, a decision, or manual action is necessary.

Lead with the result and use the user's language. Keep progress brief and informative. Store detailed state in existing project records; use the optional [stage record](templates/stage-record.md) only when no suitable record exists. Do not repeatedly ask for authorization already granted. Stop when the requested deliverables and relevant verification are complete; do not create follow-on work solely to keep the workflow running.

Specialist skills, MCP tools and workflow engines are optional execution resources, not prerequisites for this skill. Reuse available domain skills for literature, NGS, statistics, figures, specifications and writing; keep this skill responsible for the research-stage contract and final synthesis.
