# Fictional source bundle

The available data are a feature matrix with repeated rows per entity, labels and an entity identifier. Raw sensor waveforms are unavailable. The study asks whether predictions generalize to entirely unseen entities. The user requests design only. Supplied source cards are the full evidence boundary for this offline exercise; they do not establish an exhaustive search.

## Candidate A: Cedar

- Paper card A1: a fictional published article, revision 2, Methods section 3 and Supplement S1 are supplied. It fits preprocessing on training entities and evaluates on disjoint test entities. The reported metric is 0.74 on that test; transfer to the user's data is untested.
- Code relationship: the paper's code-availability statement explicitly names repository `fictional-lab/cedar` release `study-v2`. The inspected release corresponds to fictional commit `1111111111111111111111111111111111111111`.
- Inspected files: `fit.py` accepts a feature matrix, labels and entity IDs; `split.py` groups all rows from an entity; `environment.yml` pins an older environment; `LICENSE` states MIT. Supplied tests cover grouped splitting, but there is no execution receipt for the current environment.
- Repository status: archived, with no recent commits. No external weights or raw waveforms are declared. Installation compatibility has not been checked.

## Candidate B: Aurora

- Paper card B1: a fictional published abstract reports a metric of 0.93. Full methods and supplements are inaccessible in this exercise. The evaluation split and preprocessing fit scope are unknown.
- Search card B2: a fictional GitHub result advertises many stars and frequent commits for `community-example/aurora`. Its README says it is an independent implementation and cites B1. No author or publisher link confirms it as the paper's implementation.
- Inspected files: `train.py` takes raw waveform tensors; `environment.yml` describes a recent environment. No feature-matrix input path was found in these supplied files. The README reports a row-random split. A license file and native execution receipt are not supplied.

## Bounded follow-up

The user asks only what the supplied Cedar split does. The source statement is unchanged: all rows for each entity remain in one partition, with training and test entities disjoint. No implementation or data changed.
