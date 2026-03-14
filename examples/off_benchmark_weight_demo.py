from _demo_format import round_value
from pma import load_weights_csv, off_benchmark_weight

portfolio = load_weights_csv("sample-data/portfolio.csv")
benchmark = load_weights_csv("sample-data/benchmark.csv")

result = off_benchmark_weight(portfolio, benchmark)

print(round_value(result))
