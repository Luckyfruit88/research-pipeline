# State, scope and resumption

Use for long tasks, handoffs, stage changes and apparently conflicting instructions.

## Restore, then act

Find the current source of truth: project decisions, versioned schemas, current commit/worktree, input identities, job/attempt records and delivered receipts. Prior messages and memory locate those objects; stale summaries are not current acceptance.

Record the current stage's objective, deliverables, exclusions and already-authorized actions. A user's later instruction can supersede a temporary restriction, such as moving from adapter-only work to model training. Preserve that transition and its scope. An earlier authorization to merge particular changes does not authorize every later merge.

Reuse the project's state files. If none exist and the task spans interruptions, adapt the [stage record](../templates/stage-record.md). Do not maintain a second competing ledger merely because the skill ships a template.

## Block dependencies, not whole projects

For a blocker, name:
- the missing fact, artifact, resource or decision;
- the tasks and claims that depend on it;
- the evidence that would resolve it;
- authorized work that can still finish now.

A scientific HOLD can coexist with engineering progress. Equally, authorizing software development does not authorize a stronger scientific conclusion. A user-approved stage expansion changes permitted work, not the truth of earlier results.

Do not repeatedly ask for decisions already recorded. Approval must come from the user or the applicable authorization mechanism, not from elapsed time, a model review, silence or an inferred preference.

## Handoff

Leave enough state to resume without reconstructing the conversation:
- the current objective and source/input identities;
- completed capabilities and their supporting receipts;
- engineering and scientific outcomes, with limitations;
- active attempts and where to observe their terminal state;
- exact next action, blockers and any authorization still needed.

Keep status updates short and focused on new evidence. A finished requested stage needs no artificial follow-up task. Do not claim background monitoring or future contact unless the host actually provides and the user authorized that mechanism.
