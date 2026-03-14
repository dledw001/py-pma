import pytest

from pma import load_group_map_csv


def test_load_group_map_csv_loads_label_to_group_mapping(tmp_path):
    csv_filepath = tmp_path / "groups.csv"
    csv_filepath.write_text(
        "INDEX,GROUP\nAAPL,Tech\nMSFT,Tech\nXOM,Energy\n", encoding="utf-8"
    )

    result = load_group_map_csv(csv_filepath)

    assert result == {"AAPL": "Tech", "MSFT": "Tech", "XOM": "Energy"}


def test_load_group_map_csv_rejects_conflicting_duplicate_mappings(tmp_path):
    csv_filepath = tmp_path / "groups.csv"
    csv_filepath.write_text(
        "INDEX,GROUP\nAAPL,Tech\nAAPL,Energy\n", encoding="utf-8"
    )

    with pytest.raises(ValueError, match="conflicting group mappings"):
        load_group_map_csv(csv_filepath)
