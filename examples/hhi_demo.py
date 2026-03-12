from pma import load_weights_csv, hhi

portfolio = load_weights_csv("sample-data/portfolio.csv")

result = hhi(portfolio)

print(result)
