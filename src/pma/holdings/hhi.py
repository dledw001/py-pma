def hhi(portfolio_weights) -> float:
    return sum(weight * weight for weight in portfolio_weights.values())

