from _demo_format import round_value
from pma import load_weights_csv

portfolio = load_weights_csv("sample-data/portfolio.csv")

print(round_value(portfolio))
