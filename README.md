# py-pma

## usage

```python
  from pma import active_share

  portfolio = {"AAPL": 0.5, "MSFT": 0.4, "XOM": 0.1}
  benchmark = {"AAPL": 0.1, "NVDA": 0.5, "XOM": 0.4}

  result = active_share(portfolio, benchmark)
  print(result)
  ```
