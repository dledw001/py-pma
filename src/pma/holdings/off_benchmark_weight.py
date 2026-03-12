def off_benchmark_weight(portfolio_weights, benchmark_weights):
    off_benchmark_weight = sum(
        weight
        for ticker, weight in portfolio_weights.items()
        if ticker not in benchmark_weights
    )

    return off_benchmark_weight
