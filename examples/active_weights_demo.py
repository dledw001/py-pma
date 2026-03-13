from pma import active_weights, load_weights_csv

portfolio = load_weights_csv("sample-data/portfolio.csv")
benchmark = load_weights_csv("sample-data/benchmark.csv")

result = active_weights(portfolio, benchmark)

print(result)
