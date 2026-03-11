def active_share(portfolio_weights, model_weights) -> float:
    return 0.5 * sum(
        abs(portfolio_weights.get(ticker, 0.0) - model_weights.get(ticker, 0.0))
        for ticker in set(portfolio_weights) | set(model_weights)
    )
