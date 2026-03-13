import pytest

from pma import top_n_weight


def test_top_n_weight():
    portfolio = {"AAPL": 0.5, "MSFT": 0.4, "XOM": 0.1}

    n = 2
    expected_top_n_weight = 0.9

    assert top_n_weight(portfolio, n) == pytest.approx(expected_top_n_weight)
