def min_weight(portfolio_weights, include_zero_weights=False) -> float:
    """Return the smallest portfolio weight.

    This function assumes long-only normalized weights.
    """
    if include_zero_weights:
        min_weight = min(portfolio_weights.values())
    else:
        min_weight = min(v for v in portfolio_weights.values() if v > 0.0)

    return min_weight
