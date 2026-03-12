def active_weights(portfolio_weights, benchmark_weights) -> dict[str, float]:
    """Return per-security active weights versus a benchmark.

    Active weight is defined as portfolio weight minus benchmark weight
    for each security across the union of both universes.

    This function assumes long-only normalized weights.
    """
    active_weights = {
        ticker: (
            portfolio_weights.get(ticker, 0.0) - benchmark_weights.get(ticker, 0.0)
        )
        for ticker in (set(portfolio_weights) | set(benchmark_weights))
    }

    return active_weights
