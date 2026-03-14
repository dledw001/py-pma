from _demo_format import round_value
from pma import load_weights_csv, load_group_map_csv, group_weights

portfolio = load_weights_csv("sample-data/portfolio.csv")
group_map = load_group_map_csv("sample-data/group_map.csv")

result = group_weights(portfolio, group_map)

print(round_value(result))
