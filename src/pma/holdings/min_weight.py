def min_weight(portfolio_weights, *, include_zero_weights=False) -> float:
    """Return the smallest weight in a mapping.

    This function assumes long-only normalized weights.
    """
    if include_zero_weights:
        result = min(portfolio_weights.values())
    else:
        result = min(v for v in portfolio_weights.values() if v > 0.0)

    return result
