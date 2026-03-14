def overlap_weight(portfolio_weights, benchmark_weights) -> float:
    """Return the overlapping weight shared by two mappings.

    Overlap weight is defined as the sum of the smaller weights for
    each shared label.

    This function assumes long-only normalized weights.
    """
    result = sum(
        min(portfolio_weights[ticker], benchmark_weights[ticker])
        for ticker in (set(portfolio_weights) & set(benchmark_weights))
    )

    return result
