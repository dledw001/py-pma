from pma import hhi


def test_hhi():
    portfolio = {"AAPL": 0.30, "MSFT": 0.30, "JPM": 0.20, "KO": 0.20}
    result = hhi(portfolio)

    assert result == 0.26
