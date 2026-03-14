def position_count(portfolio_weights) -> int:
    """Return the number of components with strictly positive weight.

    This function assumes long-only normalized weights.
    """
    result = sum(1 for value in portfolio_weights.values() if value > 0)

    return result
