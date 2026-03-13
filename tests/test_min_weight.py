import pytest
from pma import min_weight


def test_min_weight():
    portfolio = {"AAPL": 0.5, "MSFT": 0.4, "XOM": 0.1}

    expected_min_weight = 0.1

    assert min_weight(portfolio) == pytest.approx(expected_min_weight)
