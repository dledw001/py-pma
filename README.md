# py-pma
a python library for computing portfolio management analytics.

## about

### assumptions
- currently, these functions assume long-only, normalized weights.

## usage

```python
  from pma import active_share

  portfolio = {"AAPL": 0.5, "MSFT": 0.4, "XOM": 0.1}
  benchmark = {"AAPL": 0.1, "NVDA": 0.5, "XOM": 0.4}

  result = active_share(portfolio, benchmark)
  print(result)
  ```
