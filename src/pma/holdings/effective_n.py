from .hhi import hhi


def effective_n(portfolio_weights) -> float:
    """Return the effective number of holdings in a portfolio.

    Effective N is defined as the inverse of the portfolio HHI and
    can be interpreted as a concentration-adjusted holding count.

    This function assumes long-only normalized weights.
    """
    hhi_value = hhi(portfolio_weights)
    effective_n = 1 / hhi_value

    return effective_n
