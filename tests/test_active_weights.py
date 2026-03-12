import pytest
from pma import active_weights


def test_active_weights():
    portfolio_weights = {"AAPL": 0.5, "MSFT": 0.4, "XOM": 0.1}
    benchmark_weights = {"AAPL": 0.1, "NVDA": 0.5, "XOM": 0.4}

    expected_active_weights = {"AAPL": 0.4, "MSFT": 0.4, "NVDA": -0.5, "XOM": -0.3}
    assert active_weights(portfolio_weights, benchmark_weights) == pytest.approx(
        expected_active_weights
    )
