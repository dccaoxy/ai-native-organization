"""Small explicit typed contract language, versioned as JSON; no hidden schema."""
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]
CONTRACT = json.loads((ROOT / "specs/M01.contract.json").read_text(encoding="utf-8"))


def validate(name, obj):
    definition = CONTRACT["objects"][name]
    if not isinstance(obj, dict) or set(obj) != set(definition):
        raise ValueError(name + ": exact required public fields expected")
    for key, rule in definition.items():
        value = obj[key]
        kind = rule["type"]
        valid = {"string": lambda: isinstance(value, str) and bool(value.strip()),
                 "number": lambda: type(value) in (int, float) and value >= 0,
                 "boolean": lambda: type(value) is bool,
                 "strings": lambda: isinstance(value, list) and all(isinstance(x, str) and x.strip() for x in value),
                 "object": lambda: isinstance(value, dict)}[kind]()
        if not valid or ("enum" in rule and value not in rule["enum"]):
            raise ValueError(name + "." + key + ": invalid value")
    return obj
