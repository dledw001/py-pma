# py-pma
A Python library for computing portfolio management analytics on normalized weight mappings.

## About

### Assumptions
- These functions assume long-only, normalized weights.
- `load_weights_csv` accepts raw values or pre-scaled weights and normalizes them to sum to 1.0.
- The core metrics operate on generic labeled weight mappings. In the common case, the labels are securities, but they can also be sectors, countries, industries, sleeves, or other buckets.

## Usage

```python
from pma import active_share

portfolio = {"AAPL": 0.5, "MSFT": 0.4, "XOM": 0.1}
benchmark = {"AAPL": 0.1, "NVDA": 0.5, "XOM": 0.4}

result = active_share(portfolio, benchmark)
print(result)
```

## Grouping

You can aggregate a security-level portfolio into groups and then reuse the same metrics at the grouped level.

```python
from pma import active_share, group_weights

portfolio = {"AAPL": 0.5, "MSFT": 0.4, "XOM": 0.1}
benchmark = {"AAPL": 0.1, "NVDA": 0.5, "XOM": 0.4}
sector_map = {
    "AAPL": "Information Technology",
    "MSFT": "Information Technology",
    "NVDA": "Information Technology",
    "XOM": "Energy",
}

portfolio_sectors = group_weights(portfolio, sector_map)
benchmark_sectors = group_weights(benchmark, sector_map)

result = active_share(portfolio_sectors, benchmark_sectors)
print(result)
```

`group_weights` excludes zero-weight groups by default. Pass
`include_zero_weights=True` if you want them preserved.

You can also load the weights and group mapping from separate CSV files.

```python
from pma import (
    active_share,
    group_weights,
    load_group_map_csv,
    load_weights_csv,
)

portfolio = load_weights_csv("portfolio.csv")
benchmark = load_weights_csv("benchmark.csv")
group_map = load_group_map_csv("sectors.csv")

portfolio_groups = group_weights(portfolio, group_map)
benchmark_groups = group_weights(benchmark, group_map)

result = active_share(portfolio_groups, benchmark_groups)
print(result)
```
