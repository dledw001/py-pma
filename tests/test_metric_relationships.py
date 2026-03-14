import pytest

from pma import active_share, overlap_weight


def test_active_share_equals_one_minus_overlap_weight_for_normalized_long_only_weights():
    portfolio_weights = {"AAPL": 0.5, "MSFT": 0.4, "XOM": 0.1}
    benchmark_weights = {"AAPL": 0.1, "NVDA": 0.5, "XOM": 0.4}

    assert active_share(portfolio_weights, benchmark_weights) == pytest.approx(
        1 - overlap_weight(portfolio_weights, benchmark_weights)
    )
