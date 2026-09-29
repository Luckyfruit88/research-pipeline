# Research Pipeline

[English](README.md) | [简体中文](README.zh-CN.md)

**A Codex skill for computational research design, implementation and verification.**

Research Pipeline helps turn existing data and a research question into a completed, reviewable stage. It keeps engineering progress, scientific evidence and execution authorization separate. A missing validation label can limit a scientific claim while unrelated, authorized software work continues.

## What it helps with

- Turn an existing resource inventory into a testable question and measurable endpoint.
- Design comparisons with explicit units, normalization/aggregation order, dependence, leakage controls and uncertainty.
- Build or repair research pipelines, preserving native tool semantics and failed-run evidence.
- Verify real execution, shared-compute budgets, recovery, artifact integrity and final receipts.
- Resume work without reviving obsolete stage restrictions or losing unresolved limitations.

The workflow uses an engineering-control perspective: observe the current state, define the target and constraints, act, measure and correct. This is a qualitative design discipline, not a mathematical stability or optimality guarantee.

## Example requests

~~~text
Use $research-pipeline to design a study from the datasets already available.
Define the measurable endpoint, competing explanations and feasibility checks.
~~~

~~~text
Use $research-pipeline to implement the approved missing-output prediction stage.
Keep unavailable biological validation separate from the software deliverables.
~~~

~~~text
Use $research-pipeline to investigate interrupted batches.
Recover valid products, account for the complete target list, and verify the repair.
~~~

For bounded research questions, inspect only relevant inputs, reuse still-valid checks, and stop when the requested deliverable is complete.

It does not normally activate for a standalone factual lookup, translation or prose-only edit. It complements available domain, statistics, NGS, specification and writing skills without requiring them.

## Install in Codex

Python 3.10+ and Git are needed for the installer. The skill itself has no Python runtime, service, paid API or model dependency.

~~~bash
git clone https://github.com/Luckyfruit88/research-pipeline.git
cd research-pipeline
python3 scripts/install.py
~~~

The installer copies the runtime skill into the user skill directory, normally ~/.agents/skills/research-pipeline. Existing different content is preserved; an update requires --replace and creates a backup.

To make this the default workflow for future research design and research-pipeline tasks:

~~~bash
python3 scripts/install.py --set-default
~~~

This adds a clearly marked, reversible instruction block to the personal Codex AGENTS.md. It preserves the rest of the file and does not change models, providers, credentials or approval settings. Current user/project instructions still determine scope. Automatic selection is enabled in agents/openai.yaml; already-open tasks may need to reload their context.

Use --remove-default to remove only that instruction block while leaving the skill installed. Backups are retained. A forced process kill or power loss during an update can require restoring the retained research-pipeline.backup-* directory; this installer does not claim a crash-proof multi-file transaction.

Custom locations:

~~~bash
python3 scripts/install.py --skill-home /path/to/skills --agents-file /path/to/AGENTS.md --set-default
~~~

For manual installation, copy SKILL.md, agents/, references/ and templates/ together into a folder named research-pipeline in a configured skill directory. Follow the host's current [skill documentation](https://learn.chatgpt.com/docs/build-skills).

## What “verified” means

The skill directs the agent to use real evidence and the project's executable checks. It is not an enforcement sandbox, workflow engine or scientific certification.

- Passing software tests does not validate a biological or causal claim.
- File hashes do not prove data authenticity or independence.
- Model agreement does not replace independent evidence.
- A plan, a submitted job and a successfully accounted execution are different states.

Reuse existing schemas and receipts. Add deterministic checks for material new failure modes rather than creating redundant process paperwork.

## Validation and development

~~~bash
python3 scripts/check_package.py
python3 -m unittest discover -s tests -v
~~~

Package checks cover local links, runtime files and metadata. Installer tests use temporary directories. [Behavioral cases](evals/README.md) use fabricated fixtures and do not contact a real cluster. See [the version 0.1.1 evaluation record](evals/results/v0.1.1.md) for this patch and [the initial evaluation](evals/results/v0.1.0.md) for the original forward-runs; their scopes and limitations remain separate.

For changes, keep the entrypoint small, move conditional guidance into references, and rerun the relevant behavioral cases. A reference case is a regression aid, not evidence of broad model reliability.

## Files

| Path | Purpose |
|---|---|
| SKILL.md | Main instructions and activation scope |
| references/ | Design, evidence, execution and resumption guidance |
| templates/ | Optional stage record |
| agents/openai.yaml | Codex metadata and automatic invocation policy |
| scripts/install.py | Local installation and optional default instruction |
| evals/ | Synthetic behavioral cases and evaluation record |

## Basis and license

The instructions were written from recurring computational-research and pipeline-engineering needs. Public examples are fabricated; the package contains no private project logs, unpublished study records, credentials or institution-specific paths.

Conceptual references include [Claude Scholar's research contract](https://github.com/Galaxy-Dawn/claude-scholar/blob/codex/skills/research-ideation/references/research-contract.md), [OpenSpec](https://github.com/Fission-AI/OpenSpec), [W3C PROV-DM](https://www.w3.org/TR/prov-dm/) and the [Agent Skills specification](https://agentskills.io/specification). No upstream implementation is vendored.

[MIT License](LICENSE).
