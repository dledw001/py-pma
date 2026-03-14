def max_weight(portfolio_weights) -> float:
    """Return the largest weight in a mapping.

    This function assumes long-only normalized weights.
    """
    result = max(portfolio_weights.values())

    return result
