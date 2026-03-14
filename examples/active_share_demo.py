from _demo_format import round_value
from pma import load_weights_csv, active_share

portfolio = load_weights_csv("sample-data/portfolio.csv")
benchmark = load_weights_csv("sample-data/benchmark.csv")

result = active_share(portfolio, benchmark)

print(round_value(result))
