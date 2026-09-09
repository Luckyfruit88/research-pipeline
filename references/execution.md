# Implement, run, recover and verify

Use for research code, adapters, workflow engines, shared compute and failed-run repair.

## Preflight and smallest discriminating run

Inspect the worktree, active jobs, existing outputs, project instructions and current resource/tool inventory. Reuse suitable resources before downloading or installing. A tool executable, its reference bundle and a usable input dataset are separate prerequisites.

Use the authorized branch/worktree and preserve unrelated work. Keep controlled inputs and detailed results within the approved environment. Before a public release, review the exact publishable files; do not copy private logs, host paths or study material into a generic skill or example.

Start with a bounded case that exercises the actual interface or failure mode. Keep native output, parameters and logs. Confirm coordinate/strand/allele conversions and score semantics when applicable. Retain offline synthetic tests separately from real-tool acceptance. A synthetic fixture is explicitly synthetic even when a real executable processes it.

After that diagnostic, complete the full requested stage within the approved resource envelope. Do not stop permanently at a smoke test.

## Shared compute and scheduler evidence

Discover the actual scheduler and site conventions. Do not translate Slurm examples into another scheduler by changing command names alone.

Bind the allocated CPU/memory/time envelope into the workflow executor before it starts. A nested local executor must not schedule against the entire host when only a smaller allocation was granted. Recompute admission for the current retry's resources; increasing per-task retry memory without reducing admitted concurrency can exceed the allocation.

Use explicit paths and versions where runtime behavior is fragile. Spooling schedulers may copy a wrapper; do not assume its script path identifies the source checkout. Bind the authorized checkout and full commit independently.

For Grid Engine/SGE, obtain terminal qacct records matching the job and, for arrays, the relevant task IDs. Success requires both failed=0 and exit_status=0 plus the required artifacts and checks. Missing or delayed accounting is unverified, not successful. Other schedulers require their corresponding terminal records. Queue disappearance or a success log line alone is insufficient.

An application-level test can run locally without scheduler accounting. Do not impose HPC requirements on a local-only task.

## Recovery and publication

Maintain the frozen intended task universe. Never shrink it to the outputs already accepted.

Separate:
- execution attempts, including failed attempts;
- product identity, integrity and current validity;
- summaries or indexes derived from the authoritative records.

Reconcile products from the frozen task list, receipts, logs and hashes. A stale failure summary need not invalidate an independently verified recovered product; a successful process exit does not repair a corrupt product. Report ready, failed, missing and active objects without hiding their relationship to the intended universe.

Retry or regenerate only what the evidence requires. Prefer idempotent reconciliation and incremental publication where repeated full copies are costly. Stage immutable results and atomically promote a complete version where the project needs interruption-safe publication. Do not overwrite source evidence.

Test actual interruption/recovery boundaries, resource limits and wrong-input rejection when changing those behaviors. Measure the relevant runtime, I/O, failure rate or completeness improvement; avoid presenting a cosmetic parameter change as an architecture repair.

## Final receipt and scope

Run the repository's required checks for changed code. Bind final receipts to the source/configuration and inputs actually evaluated; material changes invalidate the affected evidence.

An engineering receipt should identify the actual execution, native outputs, required checks and complete artifacts. Do not equate that receipt with empirical authenticity, biological validity or permission to merge/publish.

Deliver the runnable capability, reproducible commands, evidence locations and limitations. Complete nonblocked work before asking for a new external action. Respect already-granted publication or merge scope; do not invent a new approval gate for an action the user explicitly authorized.
