import json
import os


def generate_table(metadata):
    repo = metadata["repo"]
    problems = metadata["problems"]

    table = (
        "| Problem               | Topic   | Difficulty | Languages               |\n"
    )
    table += (
        "|-----------------------|---------|------------|-------------------------|\n"
    )

    for problem in problems:
        problem_name = problem["name"].replace("_", " ").title()
        problem_url = f"{repo}/{problem['path']}"

        language_links = [
            f"[{lang.capitalize()}]({problem_url}/{lang})"
            for lang in problem["languages"]
        ]

        table += (
            f"| [{problem_name}]({problem_url}) "
            f"| {problem['topic'].capitalize()} "
            f"| {problem['difficulty'].capitalize()} "
            f"| {', '.join(language_links)} |\n"
        )

    return table


def update_readme(metadata_file, readme_file):
    with open(metadata_file, "r") as file:
        metadata = json.load(file)

    table = generate_table(metadata)

    with open(readme_file, "r") as file:
        readme = file.readlines()

    start_marker = "<!-- START_TABLE -->\n"
    end_marker = "<!-- END_TABLE -->\n"
    start_index = readme.index(start_marker) + 1
    end_index = readme.index(end_marker)

    updated_readme = readme[:start_index] + [table] + readme[end_index:]

    with open(readme_file, "w") as file:
        file.writelines(updated_readme)


if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))

    project_root = os.path.abspath(os.path.join(script_dir, ".."))

    metadata_file = os.path.join(project_root, "metadata.json")
    readme_file = os.path.join(project_root, "README.md")

    update_readme(metadata_file, readme_file)
