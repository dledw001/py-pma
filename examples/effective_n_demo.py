from pma import load_weights_csv, effective_n

portfolio_weights = load_weights_csv("sample-data/portfolio.csv")

effective_n = effective_n(portfolio_weights)

print(effective_n)
