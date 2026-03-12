from pma import load_weights_csv, top_n_weight

portfolio_weights = load_weights_csv("sample-data/portfolio.csv")

top_n_weight = top_n_weight(portfolio_weights, 2)

print(top_n_weight)
