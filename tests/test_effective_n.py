from pma import effective_n, hhi


def test_effective_n():
    # hhi(portfolio) = 0.26
    portfolio = {"AAPL": 0.30, "MSFT": 0.30, "JPM": 0.20, "KO": 0.20}
    effective_n_value = effective_n(portfolio)

    expected_hhi = 0.26
    expected_effective_n = 1.0 / expected_hhi

    assert effective_n_value == expected_effective_n
