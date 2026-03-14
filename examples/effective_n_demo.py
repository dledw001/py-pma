from _demo_format import round_value
from pma import load_weights_csv, effective_n

portfolio_weights = load_weights_csv("sample-data/portfolio.csv")

result = effective_n(portfolio_weights)

print(round_value(result))
