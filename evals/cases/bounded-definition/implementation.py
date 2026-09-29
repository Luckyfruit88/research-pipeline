"""Fabricated definition supplied as an evaluation input, not a pipeline tool."""
from statistics import median


def summarize(rows):
    percentages = [100 * float(row["numerator"]) / float(row["denominator"])
                   for row in rows if row["eligible"] == "yes"
                   and float(row["denominator"]) > 0]
    return median(percentages) if percentages else None
