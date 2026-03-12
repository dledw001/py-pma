def hhi(portfolio_weights) -> float:
    """Return the Herfindahl-Hirschman Index (HHI) for a portfolio.

    HHI is defined as the sum of squared portfolio weights and is a
    measure of portfolio concentration.

    This function assumes long-only normalized weights.
    """
    hhi = sum(weight * weight for weight in portfolio_weights.values())

    return hhi
