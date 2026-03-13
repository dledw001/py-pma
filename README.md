# py-pma
A Python library for computing portfolio management analytics.

## About

### Assumptions
- These functions currently assume long-only, normalized weights.
- `load_weights_csv` accepts raw values or pre-scaled weights and normalizes them to sum to 1.0.

## Usage

```python
from pma import active_share

portfolio = {"AAPL": 0.5, "MSFT": 0.4, "XOM": 0.1}
benchmark = {"AAPL": 0.1, "NVDA": 0.5, "XOM": 0.4}

result = active_share(portfolio, benchmark)
print(result)
```
