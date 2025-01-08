import json
import os


def generate_table(metadata: dict) -> str:
    repo = metadata["repo"]
    problems = metadata["problems"]

    # Define table headers
    table: str = (
        "| #   | Problem               | Topic   | Difficulty | Languages               |\n"
    )
    table += "|-----|-----------------------|---------|------------|-------------------------|\n"

    for index, problem in enumerate(problems, start=1):
        problem_name: str = problem["name"].replace("_", " ").title()
        problem_url: str = f"{repo}/{problem['path']}"

        language_links: list = [
            f"[{lang.capitalize()}]({problem_url}/{lang})"
            for lang in problem["languages"]
        ]

        table += (
            f"| {index:<3} "
            f"| [{problem_name}]({problem_url}) "
            f"| {problem['topic'].capitalize()} "
            f"| {problem['difficulty'].capitalize()} "
            f"| {', '.join(language_links)} |\n"
        )

    return table


def update_readme(metadata_file: str, readme_file: str) -> None:
    with open(metadata_file, "r") as file:
        metadata = json.load(file)

    table: str = generate_table(metadata)

    with open(readme_file, "r") as file:
        readme: list = file.readlines()

    start_marker: str = "<!-- START_TABLE -->\n"
    end_marker: str = "<!-- END_TABLE -->\n"
    start_index: int = readme.index(start_marker) + 1
    end_index: int = readme.index(end_marker)

    updated_readme: list = readme[:start_index] + [table] + readme[end_index:]

    with open(readme_file, "w") as file:
        file.writelines(updated_readme)


if __name__ == "__main__":
    script_dir: str = os.path.dirname(os.path.abspath(__file__))

    project_root: str = os.path.abspath(os.path.join(script_dir, ".."))

    metadata_file: str = os.path.join(project_root, "metadata.json")
    readme_file: str = os.path.join(project_root, "README.md")

    update_readme(metadata_file, readme_file)
