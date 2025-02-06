import json
import os


def generate_summary(repo_url: str, problems: dict) -> str:
    """Generate a summary table with the total count of problems per topic."""
    topic_counts = {
        topic.replace("_", " ").title(): len(problems)
        for topic, problems in problems.items()
    }

    summary_table = "| Topic               | Number of Problems |\n"
    summary_table += "|---------------------|--------------------|\n"

    total_problems = sum(topic_counts.values())
    for topic, count in topic_counts.items():
        topic_link = f"[{topic}]({repo_url}/problems/{topic.lower().replace(' ', '_')})"
        summary_table += f"| {topic_link} | {count} |\n"

    summary_table += "|---------------------|--------------------|\n"
    summary_table += f"| **Total**          | **{total_problems}**           |\n"

    return summary_table


def generate_table_by_topic(
    repo_url: str, topic: str, difficulty_levels: dict, problems_sorted: list
) -> str:
    topic_table = f"### {topic.replace('_', ' ').capitalize()} Problems\n"
    topic_table += (
        "| #   | Problem               | Difficulty | Languages               |\n"
    )
    topic_table += (
        "|-----|-----------------------|------------|-------------------------|\n"
    )

    for index, problem in enumerate(problems_sorted, start=1):
        problem_name = problem["name"].replace("_", " ").title()
        problem_url = f"{repo_url}/problems/{topic}/{problem['name']}"

        difficulty = problem["difficulty"].lower()
        difficulty_info = difficulty_levels.get(
            difficulty, {"emoji": "⚪"}
        )  # Default: white circle
        difficulty_colored = f"<p align='center'>{difficulty_info['emoji']}</p>"

        language_links = [
            f"[{lang.capitalize()}]({problem_url}/{lang})"
            for lang in problem["languages"]
        ]

        topic_table += (
            f"| {index:<3} "
            f"| [{problem_name}]({problem_url}) "
            f"| {difficulty_colored} "
            f"| {', '.join(language_links)} |\n"
        )

    return topic_table


def generate_levels_table(difficulty_levels: dict) -> str:
    levels_table = "### Difficulty Legend\n"
    levels_table += "| Emoji | Difficulty |\n"
    levels_table += "|--------|------------|\n"
    for difficulty, info in difficulty_levels.items():
        levels_table += f"| {info['emoji']} | {difficulty.capitalize()} |\n"

    return levels_table


def generate_topic_tables(
    repo_url: str, problems: dict, difficulty_levels: dict
) -> str:
    topic_tables = ""

    # Generate a table for each topic
    for topic, problems_by_topic in problems.items():

        sorted_problems = sorted(
            problems_by_topic,
            key=lambda p: difficulty_levels.get(
                p.get("difficulty").lower(), {"rank": float("inf")}
            )["rank"],
        )
        topic_tables += generate_table_by_topic(
            repo_url, topic, difficulty_levels, sorted_problems
        )
        topic_tables += "\n"  # Add spacing between tables

    return topic_tables


def update_readme(metadata_file: str, readme_file: str) -> None:
    with open(metadata_file, "r") as file:
        metadata = json.load(file)

    difficulty_levels = {
        "easy": {"rank": 1, "emoji": "🟢"},
        "medium": {"rank": 2, "emoji": "🟡"},
        "hard": {"rank": 3, "emoji": "🔴"},
        "very hard": {"rank": 4, "emoji": "⚫"},
    }

    summary = generate_summary(metadata["repo"], metadata["problems"])
    levels_table = generate_levels_table(difficulty_levels)
    topic_tables = generate_topic_tables(
        metadata["repo"], metadata["problems"], difficulty_levels
    )

    with open(readme_file, "r") as file:
        readme = file.readlines()

    start_marker = "<!-- START_TABLE -->\n"
    end_marker = "<!-- END_TABLE -->\n"

    start_index = readme.index(start_marker) + 1
    end_index = readme.index(end_marker)

    content = f"## Summary of Problems\n\n{summary}\n{levels_table}\n{topic_tables}\n"

    # Update the README content
    updated_readme = readme[:start_index] + [content] + readme[end_index:]

    with open(readme_file, "w") as file:
        file.writelines(updated_readme)


if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))

    project_root = os.path.abspath(os.path.join(script_dir, ".."))

    metadata_file = os.path.join(project_root, "metadata.json")
    readme_file = os.path.join(project_root, "README.md")

    update_readme(metadata_file, readme_file)
