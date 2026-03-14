from .hhi import hhi


def effective_n(portfolio_weights) -> float:
    """Return the effective number of components in a weight mapping.

    Effective N is defined as the inverse of the HHI and can be
    interpreted as a concentration-adjusted component count.

    This function assumes long-only normalized weights.
    """
    hhi_value = hhi(portfolio_weights)
    result = 1 / hhi_value

    return result
