from pma import load_weights_csv, active_share

portfolio = load_weights_csv("sample-data/portfolio.csv")
model = load_weights_csv("sample-data/model.csv")

active_share = active_share(portfolio, model)

print(active_share)
