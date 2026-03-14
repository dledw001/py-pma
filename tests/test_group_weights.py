import pytest

from pma import group_weights


def test_group_weights_aggregates_labels_into_groups():
    weights = {"AAPL": 0.3, "MSFT": 0.4, "XOM": 0.3}
    group_map = {
        "AAPL": "Tech",
        "MSFT": "Tech",
        "XOM": "Energy",
    }

    result = group_weights(weights, group_map)

    assert result == pytest.approx({"Tech": 0.7, "Energy": 0.3})


def test_group_weights_errors_on_missing_mapping_by_default():
    weights = {"AAPL": 0.5, "MSFT": 0.5}
    group_map = {"AAPL": "Tech"}

    with pytest.raises(ValueError, match="missing group mapping"):
        group_weights(weights, group_map)


def test_group_weights_can_drop_unmapped_labels():
    weights = {"AAPL": 0.5, "MSFT": 0.5}
    group_map = {"AAPL": "Tech"}

    result = group_weights(weights, group_map, missing="drop")

    assert result == pytest.approx({"Tech": 0.5})


def test_group_weights_can_bucket_unmapped_labels_as_unknown():
    weights = {"AAPL": 0.5, "MSFT": 0.5}
    group_map = {"AAPL": "Tech"}

    result = group_weights(weights, group_map, missing="unknown")

    assert result == pytest.approx({"Tech": 0.5, "Unknown": 0.5})


def test_group_weights_excludes_zero_weight_groups_by_default():
    weights = {"AAPL": 0.5, "TSLA": 0.0}
    group_map = {"AAPL": "Tech", "TSLA": "Consumer Discretionary"}

    result = group_weights(weights, group_map)

    assert result == pytest.approx({"Tech": 0.5})


def test_group_weights_can_preserve_zero_weight_groups():
    weights = {"AAPL": 0.5, "TSLA": 0.0}
    group_map = {"AAPL": "Tech", "TSLA": "Consumer Discretionary"}

    result = group_weights(weights, group_map, include_zero_weights=True)

    assert result == pytest.approx({"Tech": 0.5, "Consumer Discretionary": 0.0})
