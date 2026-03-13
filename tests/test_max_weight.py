import pytest
from pma import max_weight


def test_max_weight():
    portfolio = {"AAPL": 0.5, "MSFT": 0.4, "XOM": 0.1}

    expected_max_weight = 0.5

    assert max_weight(portfolio) == pytest.approx(expected_max_weight)
