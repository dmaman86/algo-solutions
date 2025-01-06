import argparse
import subprocess
from pathlib import Path


def main(save_results_flag: bool):
    root_dir = Path(__file__).resolve().parents[2]
    test_dir = root_dir / "tests" / "python"

    scripts = [
        script
        for script in test_dir.rglob("*.py")
        if script.name.startswith("test_") and script.name != "test_runner.py"
    ]

    for script in scripts:
        print(f"Running {script}...")
        subprocess.run(
            ["python", str(script), "--save-results" if save_results_flag else ""],
            check=True,
            cwd=root_dir,
        )


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run all test scripts.")
    parser.add_argument(
        "--save-results",
        action="store_true",
        help="Save the results of the test cases to a JSON file.",
    )
    args = parser.parse_args()
    main(save_results_flag=args.save_results)
