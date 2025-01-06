import json
from pathlib import Path


def load_json(filename: str) -> list[dict]:
    root_dir = Path(__file__).resolve().parents[1]
    json_path = root_dir / "tests" / filename

    if not json_path.exists():
        raise FileNotFoundError(f"File not found: {json_path}")

    with open(json_path, "r") as file:
        return json.load(file)
