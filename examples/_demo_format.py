def round_value(value, digits=3):
    if isinstance(value, float):
        return round(value, digits)

    if isinstance(value, dict):
        return {key: round_value(inner, digits) for key, inner in value.items()}

    if isinstance(value, list):
        return [round_value(item, digits) for item in value]

    if isinstance(value, tuple):
        return tuple(round_value(item, digits) for item in value)

    return value
