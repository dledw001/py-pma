def off_benchmark_weight(portfolio_weights, benchmark_weights) -> float:
    """Return the total weight absent from the benchmark mapping.

    This function assumes long-only normalized weights.
    """
    result = sum(
        weight
        for ticker, weight in portfolio_weights.items()
        if ticker not in benchmark_weights
    )

    return result
