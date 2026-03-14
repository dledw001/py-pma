import csv


def load_weights_csv(csv_filepath) -> dict[str, float]:
    """Load labeled values from CSV and return normalized weights.

    The CSV must contain ``INDEX`` and ``VALUE`` columns. Duplicate labels
    are aggregated before the final weights are normalized to sum to 1.0.
    """
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


def load_group_map_csv(csv_filepath) -> dict[str, str]:
    """Load label-to-group mappings from CSV.

    The CSV must contain ``INDEX`` and ``GROUP`` columns. Duplicate labels
    are not allowed because each label must map to a single group.
    """
    group_map = {}

    with open(csv_filepath, newline="") as csv_file:
        reader = csv.DictReader(csv_file)

        if reader.fieldnames is None:
            raise ValueError(f"{csv_filepath} is empty")

        required_columns = {"INDEX", "GROUP"}
        missing_columns = required_columns - set(reader.fieldnames)
        if missing_columns:
            raise ValueError(
                f"{csv_filepath} is missing required columns: {sorted(missing_columns)}"
            )

        for row in reader:
            label = row["INDEX"]
            group = row["GROUP"]

            if label is None or group is None:
                raise ValueError(
                    f"{csv_filepath} contains a row with missing required data"
                )

            label = label.strip()
            group = group.strip()

            if not label:
                raise ValueError(f"{csv_filepath} contains a blank label")
            if not group:
                raise ValueError(f"{csv_filepath} contains a blank group")

            if label in group_map and group_map[label] != group:
                raise ValueError(
                    f"{csv_filepath} has conflicting group mappings for {label!r}"
                )

            group_map[label] = group

    return group_map
