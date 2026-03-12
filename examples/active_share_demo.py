from pma import load_weights_csv, active_share

portfolio = load_weights_csv("sample-data/portfolio.csv")
benchmark = load_weights_csv("sample-data/benchmark.csv")

active_share = active_share(portfolio, benchmark)

print(active_share)
