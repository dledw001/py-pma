def min_weight(portfolio_weights) -> float:
    """Return the smallest portfolio weight.

    This function assumes long-only normalized weights.
    """
    min_weight = min(portfolio_weights.values())
    return min_weight
