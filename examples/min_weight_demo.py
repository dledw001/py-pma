from pma import load_weights_csv, min_weight

portfolio = load_weights_csv("sample-data/portfolio.csv")

result_exclude_zero_weights = min_weight(portfolio)
result_include_zero_weights = min_weight(portfolio, include_zero_weights=True)

print(result_exclude_zero_weights)
print(result_include_zero_weights)
