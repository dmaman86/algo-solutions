import json
from pathlib import Path


def load_test_cases(filename: str) -> list[dict]:
    root_dir = Path(__file__).resolve().parents[1]
    json_path = root_dir / "test_cases" / filename

    if not json_path.exists():
        raise FileNotFoundError(f"File not found: {json_path}")

    with open(json_path, "r") as file:
        return json.load(file)


def save_results(filename: str, results: list[dict]) -> None:
    root_dir = Path(__file__).resolve().parents[1]
    json_path = root_dir / "results" / filename

    json_path.parent.mkdir(parents=True, exist_ok=True)

    with open(json_path, "w") as file:
        json.dump(results, file, indent=4)
