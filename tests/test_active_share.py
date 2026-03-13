import pytest
from pma import active_share


def test_active_share():
    portfolio = {"AAPL": 0.5, "MSFT": 0.4, "XOM": 0.1}
    benchmark = {"AAPL": 0.5, "MSFT": 0.4, "XOM": 0.1}

    expected_active_share = 0.0
    assert active_share(portfolio, benchmark) == pytest.approx(expected_active_share)
