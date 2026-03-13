from pma import load_weights_csv, position_count

portfolio = load_weights_csv("sample-data/portfolio.csv")

result = position_count(portfolio)

print(result)
