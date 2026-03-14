def group_weights(
    weights,
    group_map,
    *,
    missing="error",
    unknown_group="Unknown",
    include_zero_weights=False,
) -> dict[str, float]:
    """Aggregate weights into named groups.

    ``weights`` is a mapping from component label to normalized weight.
    ``group_map`` maps each component label to a group label such as a
    sector, country, industry, or strategy bucket.

    By default, every component must have a mapping. Unmapped components
    can instead be dropped or assigned to ``unknown_group``. Zero-weight
    groups are excluded by default.
    """
    if missing not in {"error", "drop", "unknown"}:
        raise ValueError("missing must be one of: 'error', 'drop', 'unknown'")

    grouped_weights = {}

    for label, weight in weights.items():
        group = group_map.get(label)

        if group is None:
            if missing == "error":
                raise ValueError(f"missing group mapping for {label!r}")
            if missing == "drop":
                continue
            group = unknown_group

        grouped_weights[group] = grouped_weights.get(group, 0.0) + weight

    if include_zero_weights:
        return grouped_weights

    return {
        group: weight for group, weight in grouped_weights.items() if weight != 0.0
    }
