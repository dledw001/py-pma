from _demo_format import round_value
from pma import load_weights_csv, max_weight

portfolio_weights = load_weights_csv("sample-data/portfolio.csv")

result = max_weight(portfolio_weights)

print(round_value(result))
