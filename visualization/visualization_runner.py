import subprocess
import sys
from pathlib import Path


def main():
    root_dir = Path(__file__).resolve().parents[1]
    sys.path.append(str(root_dir))
    visualization_dir = root_dir / "visualization"

    scripts = [
        script
        for script in visualization_dir.rglob("*.py")
        if script.parent != visualization_dir
    ]

    for script in scripts:
        print(f"Running {script}...")
        subprocess.run(["python", script], check=True, cwd=root_dir)


if __name__ == "__main__":
    main()
