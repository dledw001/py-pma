def position_count(portfolio_weights) -> int:
    """Return the number of holdings with strictly positive weight.

    This function assumes long-only normalized weights.
    """
    position_count = sum(1 for value in portfolio_weights.values() if value > 0)
    return position_count
