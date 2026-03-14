import pytest

from pma import overlap_weight


def test_overlap_weight():
    portfolio_weights = {"AAPL": 0.5, "MSFT": 0.4, "XOM": 0.1}
    benchmark_weights = {"AAPL": 0.4, "MSFT": 0.5, "XOM": 0.1}

    expected_overlap_weight = 0.9
    assert overlap_weight(portfolio_weights, benchmark_weights) == pytest.approx(
        expected_overlap_weight
    )
