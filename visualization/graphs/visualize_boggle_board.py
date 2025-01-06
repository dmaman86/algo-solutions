from io import BytesIO
from pathlib import Path

import matplotlib.pyplot as plt
from fpdf import FPDF

from visualization.utility import load_json


def visualize_boggle_board_image(
    pdf: FPDF, board: list[list[str]], words: list[str], result: dict, test_name: str
) -> None:
    fig, axs = plt.subplots(2, 1, figsize=(14, 8))

    fig.suptitle(f"Boggle Board Test Case: {test_name}")

    axs[0].set_title("Boggle Board")
    cell_size = 1
    for i, row in enumerate(board):
        for j, letter in enumerate(row):
            x, y = j, len(board) - i - 1
            color = (
                "lightgreen"
                if (i, j)
                in {
                    tuple(pos)
                    for positions in result["words"].values()
                    for pos in positions
                }
                else "white"
            )
            axs[0].add_patch(
                plt.Rectangle(
                    (x, y),
                    cell_size,
                    cell_size,
                    facecolor=color,
                    edgecolor="black",
                    linewidth=1.5,
                )
            )
            axs[0].text(x + 0.5, y + 0.5, letter, ha="center", va="center", fontsize=12)

    axs[0].set_xlim(0, len(board[0]))
    axs[0].set_ylim(0, len(board))
    axs[0].axis("off")

    axs[1].set_title("Word List")
    axs[1].axis("off")

    y_start = 0.9
    y_step = 0.05
    found_words = set(result["words"].keys())
    for i, word in enumerate(words):
        if word in found_words:
            positions = result["words"][word]
            text = f"{word} - {positions}"
            color = "black"
        else:
            text = word
            color = "red"

        axs[1].text(
            0.5,
            y_start - i * y_step,
            text,
            fontsize=12,
            color=color,
            va="top",
            ha="center",
        )

    image_path = Path(f"{test_name}.png")
    plt.savefig(image_path, bbox_inches="tight")
    plt.close()

    pdf.add_page()
    pdf.image(str(image_path), x=10, y=10, w=190)
    image_path.unlink()


def visualize_boggle_board(test_cases_file: str, results_file: str) -> None:

    test_cases = load_json(test_cases_file)
    results = load_json(results_file)
    pdf = FPDF()

    for idx, (test, result) in enumerate(zip(test_cases, results)):
        board = test["board"]
        words = test["words"]
        test_name = f"test_case_{idx}"

        visualize_boggle_board_image(pdf, board, words, result, test_name)

    root_dir = Path(__file__).parents[2] / "output_images"
    base_path = root_dir / "graphs" / "boggle_board"
    base_path.mkdir(parents=True, exist_ok=True)

    output_file = base_path / "boggle_results.pdf"
    pdf.output(name=str(output_file))
    print(f"PDF file saved at: {output_file}")


def main():
    test_cases_file = "test_cases/graphs/boggle_board.json"
    results_file = "results/graphs/boggle_board.json"

    visualize_boggle_board(test_cases_file, results_file)


if __name__ == "__main__":
    main()
