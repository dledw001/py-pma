from pma import position_count


def test_position_count():
    portfolio = {"AAPL": 0.50, "MSFT": 0.40, "XOM": 0.10, "CASH": 0.00}
    result = position_count(portfolio)

    assert result == 3
