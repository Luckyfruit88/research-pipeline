# Behavioral evaluations

These cases use entirely fabricated names, counts, paths and research objects. They exercise transferable failure modes, not any private project's data or conclusions.

Run each case in a fresh agent context with SKILL.md and the minimum case inputs. Give the agent the corresponding TASK.md. Use a temporary output directory outside the repository. Do not give the evaluator rubric or prior evaluation results to the agent doing the task.

No network, real cluster, paid computation, external communication or persistent installation is needed. The run should stay within the case directory and temporary outputs.

| Case | Task |
|---|---|
| stage-transition | Resume a stage whose scope changed after an inconclusive scientific comparison |
| measurement-design | Design a study when marginal measurements may not identify a proposed joint endpoint |
| interrupted-run | Reconcile a finite workload from artifacts, accounting and a stale summary |
| bounded-definition | Explain the implemented unit-level summary without broadening the task |
| check-reuse | Distinguish reusable checks from results invalidated by changed inputs |

Afterward, inspect the actual artifacts using [the rubric](rubric.md). Keep engineering observations separate from scientific validity. Record model/runtime, input scope, failures, revisions and limitations in the versioned evaluation record. Do not report an unrun case as passing.
