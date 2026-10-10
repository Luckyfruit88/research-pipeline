"""Fabricated cohort feature-selection example; not a production pipeline."""
from collections import Counter
import json
from pathlib import Path


def select_features(samples):
    support = Counter(feature for row in samples for feature, value in row.items() if value > 0)
    return sorted(feature for feature, count in support.items() if count >= 2)


if __name__ == "__main__":
    case = json.loads(Path(__file__).with_name("recovery.json").read_text())
    rows = [case["toy_complete_counts_for_counterexample"][sample] for sample in case["frozen_order"]]
    joint = select_features(rows)
    separate = sorted({feature for row in rows for feature in select_features([row])})
    print(json.dumps({"joint_features": joint, "separate_then_concatenated": separate,
                      "equivalent": joint == separate, "recovery_jobs_executed": False}))
