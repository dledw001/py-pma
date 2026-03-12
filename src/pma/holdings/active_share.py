def active_share(portfolio_weights, model_weights) -> float:
    """Return the active share between a portfolio and a benchmark.

    Active share is defined as half the sum of absolute differences
    between portfolio and benchmark weights across all securities.

    This function assumes long-only normalized weights.
    """
    active_share = 0.5 * sum(
        abs(portfolio_weights.get(ticker, 0.0) - model_weights.get(ticker, 0.0))
        for ticker in set(portfolio_weights) | set(model_weights)
    )

    return active_share
