from pma import off_benchmark_weight


def test_off_benchmark_weight():
    portfolio = {"AAPL": 0.5, "MSFT": 0.4, "XOM": 0.1}
    benchmark = {"AAPL": 0.1, "NVDA": 0.5, "XOM": 0.4}

    expected_off_benchmark_weight = 0.4

    assert off_benchmark_weight(portfolio, benchmark) == expected_off_benchmark_weight
