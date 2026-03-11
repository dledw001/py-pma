from .io import load_weights
from .active_share import compute_active_share

portfolio = load_weights("sample-data/portfolio.csv")
model = load_weights("sample-data/model.csv")

active_share = compute_active_share(portfolio, model)

print(active_share)
