import pytest

from pma import load_weights_csv


def test_load_weights_csv_normalizes_and_aggregates_duplicates(tmp_path):
    csv_filepath = tmp_path / "weights.csv"
    csv_filepath.write_text(
        "INDEX,VALUE\nAAPL,50\nMSFT,30\nAAPL,20\n", encoding="utf-8"
    )

    result = load_weights_csv(csv_filepath)

    assert result == pytest.approx({"AAPL": 0.7, "MSFT": 0.3})
