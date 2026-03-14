def active_weights(portfolio_weights, benchmark_weights) -> dict[str, float]:
    """Return per-component active weights versus a benchmark.

    Active weight is defined as portfolio weight minus benchmark weight
    for each label across the union of both mappings.

    This function assumes long-only normalized weights.
    """
    result = {
        ticker: (
            portfolio_weights.get(ticker, 0.0) - benchmark_weights.get(ticker, 0.0)
        )
        for ticker in (set(portfolio_weights) | set(benchmark_weights))
    }

    return result
