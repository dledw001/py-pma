def max_weight(portfolio_weights) -> float:
    """Return the largest portfolio weight.

    This function assumes long-only normalized weights.
    """
    max_weight = max(portfolio_weights.values())

    return max_weight
