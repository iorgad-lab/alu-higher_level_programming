#!/usr/bin/python3
"""Module that returns the weighted average of a list of tuples."""


def weight_average(my_list=[]):
    """Return the weighted average of (score, weight) tuples."""
    if len(my_list) == 0:
        return 0

    total_weight = 0
    total_score = 0

    for score, weight in my_list:
        total_score += score * weight
        total_weight += weight

    if total_weight == 0:
        return 0

    return total_score / total_weight
