from pma import load_weights_csv, overlap_weight

portfolio = load_weights_csv("sample-data/portfolio.csv")
benchmark = load_weights_csv("sample-data/benchmark.csv")

result = overlap_weight(portfolio, benchmark)

print(result)
