# Find research and implementations for a design decision

Use during study design or method selection when prior research and reusable code affect novelty, measurement or feasibility. The output is a supported design choice and next check, not just a reading list.

## Bound and perform the search

Identify the decision to resolve, the available data, the required endpoint and the material unknowns. Search by the scientific question, method family and input/output requirements. Use available scholarly databases, repository connectors or web search and browsing; no particular provider, plugin or API key is required. Actually retrieve sources rather than describing a search that has not happened. Keep restricted data and unpublished identifying details out of external queries.

Search primary papers and their supplementary material, then follow data/code availability links to implementations. Also search GitHub for the relevant method or paper to find maintained implementations and alternatives. Use reviews and search snippets to locate sources; inspect the primary material before attributing a claim to it. Reuse verified sources and relevant specialist tools without installing a new search stack by default.

Bound the search by the current decision, source classes and unresolved questions. Record the queries, retrieval date, sources inspected and access gaps in the existing design record. Stop when the material choices can be compared and the remaining gaps have a concrete next check, or the stated search boundary is reached. Do not infer novelty or the absence of code from a failed keyword search; report what was not found within the searched scope. If retrieval is restricted or unavailable, use the supplied evidence and label unverified choices as provisional.

## Read the scientific evidence

For each serious candidate, retain a stable paper identifier or URL, version/publication status and the exact section, table or supplement supporting the decision. Distinguish published papers from preprints; check relevant corrections or retractions when relying on the reported findings. Say whether the evidence was full text, a supplement or abstract-only.

Extract the scientific question, population or assay, input requirements, measurement unit, endpoint, key assumptions and validation design. Examine the comparators, split/dependence rules, uncertainty and limitations that matter for the proposed use. A headline metric does not establish transfer to a different assay, population or evaluation split. Missing methods or inaccessible supplements remain evidence gaps.

## Check the implementation relationship and fit

Establish whether a repository is author-linked code, a community reimplementation, a fork or an unrelated namesake. Record the evidence for that relationship; a matching name or citation alone does not prove that this code generated the paper's results.

For shortlisted repositories, pin a release or commit and inspect the relevant entrypoint, configuration and environment files. Check the license or its absence, maintenance/archival status, required references, weights and data, input/output semantics, compute requirements and available tests or run evidence. Report what was inspected and what remains unknown. A public repository or code license does not establish access to its required data or permission to redistribute them.

Use maintenance activity to assess operational risk, not scientific correctness. An older stable implementation can fit better than a popular recent one. Compare method and repository versions, assumptions and output definitions; record discrepancies rather than silently substituting one implementation for another. Keep documented support, source inspection and a successful run as separate evidence levels. A design task does not itself require installation, training, large downloads or executing setup scripts; run a bounded check only within the current authorization.

## Convert the evidence into a decision

Use a compact comparison in the existing design deliverable; omit irrelevant fields:

| Candidate and scientific evidence | Repository, version and relationship | Fit to available data and endpoint | Limitations and missing evidence | Next discriminating check |
|---|---|---|---|---|
| [method; paper and section/supplement] | [URL; commit/release; evidence level] | [compatible requirements or mismatch] | [scientific and operational gaps] | [smallest useful check and authorization] |

Recommend a path based on evidence and fit, preserving the user's requested comparison range. Explain what to reuse, what needs adaptation and what observation would change the choice. Keep scientific credibility, implementation readiness and project suitability distinct. If no implementation is suitable, distinguish a feasible reimplementation from a method whose required information is unavailable. Feed the result back into the design's endpoint, baseline, feasibility and validation plan.
