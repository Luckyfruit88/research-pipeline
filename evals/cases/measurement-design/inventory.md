# Fabricated resource inventory

The locus is GENE_DEMO, and the two boundary choices are D0/D1 and A0/A1. The marker is VAR_DEMO.

Available:
- A versioned table of marginal donor-boundary counts.
- A separate versioned table of marginal acceptor-boundary counts.
- Participant identifiers connecting libraries; some participants have two technical libraries.
- WGS genotype calls and BAM/CRAM access are listed in the inventory, but have not been opened in this exercise.
- A small metadata sample shows paired reads, 100 bases per mate.
- Reference annotation lists four possible endpoint combinations.
- 240 table rows come from 12 libraries and 8 participants.

Unknown:
- Marker heterozygote count and relatedness among participants.
- Physical fragment linkage of marker, donor and acceptor.
- Fragment recovery, mapping/allelic bias, ambiguous paths and actual joint counts.
- Whether the annotation combinations are observed in these libraries.
- Batch-specific depth and the variance needed for precision planning.

Only design and a bounded first measurement specification are authorized. No public data transfer, full cohort analysis or causal interpretation has been authorized.
