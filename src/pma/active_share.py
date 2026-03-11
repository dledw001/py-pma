import csv


def compute_active_share(portfolio_weights, model_weights) -> float:
    return 0.5 * sum(
        abs(portfolio_weights.get(ticker, 0.0) - model_weights.get(ticker, 0.0))
        for ticker in set(portfolio_weights) | set(model_weights)
    )


def load_weights(csv_filepath) -> dict[str, float]:
    totals_by_ticker = {}

    with open(csv_filepath, newline="") as csv_file:
        reader = csv.DictReader(csv_file)

        if reader.fieldnames is None:
            raise ValueError(f"{csv_filepath} is empty")

        required_columns = {"INDEX", "VALUE"}
        missing_columns = required_columns - set(reader.fieldnames)
        if missing_columns:
            raise ValueError(
                f"{csv_filepath} is missing required columns: {sorted(missing_columns)}"
            )

        for row in reader:
            ticker = row["INDEX"]
            raw_value = row["VALUE"]

            if ticker is None or raw_value is None:
                raise ValueError(
                    f"{csv_filepath} contains a row with missing required data"
                )

            ticker = ticker.strip()
            if not ticker:
                raise ValueError(f"{csv_filepath} contains a blank ticker")

            try:
                value = float(raw_value)
            except ValueError as exc:
                raise ValueError(
                    f"{csv_filepath} has a non-numeric VALUE for {ticker!r}"
                ) from exc

            totals_by_ticker[ticker] = totals_by_ticker.get(ticker, 0.0) + value

    total_value = sum(totals_by_ticker.values())
    if total_value <= 0:
        raise ValueError(f"{csv_filepath} total must be > 0")

    return {ticker: value / total_value for ticker, value in totals_by_ticker.items()}
