from io import BytesIO
from pathlib import Path

import matplotlib.pyplot as plt
from boggle_board.python.boggle_board import boggleBoard
from fpdf import FPDF
from fpdf.enums import XPos, YPos
from utility import load_test_cases


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
                in {pos for positions in result["words"].values() for pos in positions}
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


def visualize_boggle_board_pdf(
    board: list[list[str]],
    words: list[str],
    result: dict,
    file_name: str,
    output_dir: str = "output_images",
) -> None:
    base_path = Path(__file__).parent / output_dir
    base_path.mkdir(parents=True, exist_ok=True)

    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    pdf.set_font("Helvetica", size=12)

    cell_size = 10
    start_x, start_y = 10, pdf.get_y() + 10

    highlightes_positions = set()
    for positions in result["words"].values():
        highlightes_positions.update(positions)

    for i, row in enumerate(board):
        for j, letter in enumerate(row):
            x = start_x + j * cell_size
            y = start_y + i * cell_size

            if (i, j) in highlightes_positions:
                pdf.set_fill_color(200, 230, 201)
                pdf.rect(x, y, cell_size, cell_size, style="DF")
            else:
                pdf.rect(x, y, cell_size, cell_size, style="D")

            pdf.set_xy(x, y)
            pdf.cell(cell_size, cell_size, letter, align="C")

    pdf.set_y(start_y + len(board) * cell_size + 10)
    pdf.set_font("Helvetica", "B", size=12)
    pdf.cell(0, 10, "Word List:", new_x=XPos.LMARGIN, new_y=YPos.NEXT)

    pdf.set_font("Helvetica", size=12)
    for word in words:
        pdf.cell(0, 10, word, new_x=XPos.LMARGIN, new_y=YPos.NEXT)

    output_file = base_path / f"{file_name}.pdf"
    pdf.output(name=str(output_file))
    print(f"PDF file saved at: {output_file}")


def test_boggle_board() -> None:

    test_cases = load_test_cases("graphs/boggle_board.json")
    pdf = FPDF()

    for idx, test in enumerate(test_cases):
        board = test["board"]
        words = test["words"]
        expected = test["expected"]

        result = boggleBoard(board, words)
        test_name = f"test_case_{idx}"

        visualize_boggle_board_image(pdf, board, words, result, test_name)

        # visualize_boggle_board_pdf(board, words, result, filename)
        assert set(result["words"].keys()) == set(
            expected
        ), f"Test case failed at index {idx}!"

    output_file = Path(__file__).parent / "boggle_results.pdf"
    pdf.output(name=str(output_file))
    print(f"PDF file saved at: {output_file}")
