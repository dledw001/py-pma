def hhi(portfolio_weights) -> float:
    """Return the Herfindahl-Hirschman Index (HHI) for a weight mapping.

    HHI is defined as the sum of squared weights and is a measure of
    concentration.

    This function assumes long-only normalized weights.
    """
    result = sum(weight * weight for weight in portfolio_weights.values())

    return result
