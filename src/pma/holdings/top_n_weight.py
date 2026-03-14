def top_n_weight(portfolio_weights, n) -> float:
    """Return the combined weight of the top N components.

    Components are ranked from largest to smallest weight before the
    top N weights are summed.

    This function assumes long-only normalized weights.
    """
    sorted_weights = sorted(portfolio_weights.values(), reverse=True)
    result = sum(sorted_weights[:n])

    return result
