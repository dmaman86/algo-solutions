from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

from problems.graphs.minimum_passes_of_matrix.python.minimum_passes_of_matrix import \
    minimum_passes_of_matrix
from tests.python.utility import load_test_cases


def draw_table(matrix: list[list[int]], ax: plt.Axes) -> None:
    table = ax.table(cellText=matrix, cellLoc="center", loc="center")
    nrows, ncols = len(matrix), len(matrix[0])
    for _, cell in table.get_celld().items():
        cell.set_height(1 / nrows)
        cell.set_width(1 / ncols)


def visualize_passes(
    history: dict[int, list[list[int]]], passes: int, filename: str
) -> None:
    root_dir = Path(__file__).resolve().parent
    base_path = root_dir / "minimum_passes_of_matrix_images"
    base_path.mkdir(parents=True, exist_ok=True)

    if passes <= 0:
        fig, ax = plt.subplots(figsize=(10, 5))
        ax.set_title("Matrix could not be fully converted.", fontsize=16)
        ax.axis("off")
        draw_table(history[0], ax)

    else:
        total_passes = len(history)
        rows = max((total_passes // 2) + (total_passes % 2), 1)
        cols = 2

        fig, axes = plt.subplots(rows, cols, figsize=(10, 5 * rows))
        axes = axes.flatten()

        for idx, (p, matrix) in enumerate(history.items()):
            ax = axes[idx]
            title = f"Pass {p}" if idx > 0 else "Initial Matrix"
            ax.set_title(title, fontsize=16)
            ax.axis("off")
            draw_table(matrix, ax)

        for idx in range(total_passes, len(axes)):
            axes[idx].axis("off")

    output_file = base_path / f"{filename}.png"
    plt.savefig(output_file, format="png", bbox_inches="tight")
    plt.close()
    print(f"Visualized image at {output_file}")


def test_minimum_passes_of_matrix(visualize: bool) -> None:

    test_cases = load_test_cases("graphs/minimum_passes_of_matrix.json")

    for idx, test in enumerate(test_cases):
        matrix = test["matrix"]
        expected = test["expected"]

        passes, history = minimum_passes_of_matrix(matrix)

        assert passes == expected, f"Test case failed at index {idx}"

        if visualize:
            visualize_passes(history, passes, f"test_case_{idx}")
