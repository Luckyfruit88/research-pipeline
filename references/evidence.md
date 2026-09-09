# Evidence, dependence and evaluation

Use for dataset construction, model evaluation, scientific audits and claim review.

## Two relationship systems

Keep distinct:
1. **Derivation/provenance:** which source, transformation, tool, parameter set or observation produced a value?
2. **Validation dependence:** which constructs, positions, genes, participants, experiments, batches or homologous groups must remain together or be represented in uncertainty?

Sharing a reference assembly or predictor does not connect every sample into one statistical group. Different filenames, accessions, source IDs or exports do not establish independent data. Distinguish feature correlation, shared measurement, computational derivation and target leakage; they call for different remedies.

Record unknown relationships explicitly and state which claim they limit. Do not solve target leakage merely by down-weighting a feature.

## Identity and units

Follow existing project conventions. Relevant identities can include source accessions and versions, content hashes, reference/annotation, coordinate and allele conventions, assay context, experimental units, native tool parameters, transformations and frozen split rules.

Preserve one-to-many mappings, ambiguous records and exclusion reasons. Report the flow from observations to paired objects, correlation groups, experimental units and external sources. Do not label any one count the effective sample size without a model that justifies it.

Keep experiment specification identity separate from attempt identity. If results are content-addressed, include all outcome-relevant identities or bind them by verified references: code, data, reference resources, resolved configuration, parameters/model revision, environment and evaluation protocol. Recording a field in a manifest does not prove it participated in the identifier or execution.

## Training exposure and holdout

For the fixed tool/model version, distinguish target-label exposure, construct or allele exposure, sequence/locus exposure, possible shared source pools and unknown membership. Apply exclusions or claims proportionately.

Fit transformations, filtering decisions, feature selection and method tuning only on permitted development data. Preserve the required groups across splits, including relevant cross-partition homology. Never call already-inspected test data a fresh independent test.

When an external tool's training set cannot be recovered, label uncertainty and perform the prespecified analysis that is still defensible. Do not invent membership or treat a broad public source pool as confirmed training exposure.

## Missing inputs and multiple outputs

Define each task's units, context, denominator and label origin. Distinguish predicting a native tool's output from predicting an experimental measurement. Success on the former does not validate the latter.

Use observed labels for the corresponding loss. Unfitted or unsupported tasks must remain unavailable or abstain, not return fabricated values. Include input masks and justified QC/context information without leaking target presence or values.

When hiding a source, remove equivalent and derived information, including REF/ALT/differences and all dependent descendants where relevant. Independently verify that target-equivalent transformations of the same measurement have not re-entered the inputs.

Evaluate complete inputs, prespecified missing-source combinations, natural unsupported contexts and abstention. Artificial masking does not represent every real missingness mechanism. Report errors and coverage together; a favorable intersection of successful predictions can conceal failures.

## Claims and independent checks

For each consequential claim, record evidence, allowed wording, stronger unsupported wording, contradictions, limitations and the next discriminating measurement.

Report uncertainty at the relevant dependent unit; technical reruns are not biological replication. Separate information gain from changed coverage, tool agreement from experimental validation, and association from mechanism.

Use independent reconstruction or comparison when a transform, migration or scientific gate needs it. Reusing the same algorithm or asking another model to agree is not automatically independent verification. Distinct models may help find problems; the conclusion must still be grounded in primary evidence and appropriate executable checks.

Useful standards and implementation references:
- [W3C PROV-DM](https://www.w3.org/TR/prov-dm/) for provenance concepts.
- [scikit-learn: common pitfalls](https://scikit-learn.org/stable/common_pitfalls.html) for preprocessing and leakage.
- [scikit-learn: grouped cross-validation](https://scikit-learn.org/stable/modules/cross_validation.html#cross-validation-iterators-for-grouped-data) for available grouped split mechanisms. Select a method appropriate to the study; a library splitter alone does not establish independence.
