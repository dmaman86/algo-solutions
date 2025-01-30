import json
import os


def generate_summary(metadata: dict) -> str:
    """Generate a summary table with the total count of problems per topic."""
    repo = metadata["repo"]
    problems = metadata["problems"]

    # Count problems by topic
    topic_counts = {}
    for problem in problems:
        topic = problem.get("topic", "Unknown").capitalize()
        topic_counts[topic] = topic_counts.get(topic, 0) + 1

    # Generate the table
    summary_table = "| Topic               | Number of Problems |\n"
    summary_table += "|---------------------|--------------------|\n"

    total_problems = 0
    for topic, count in topic_counts.items():
        topic_link = f"[{topic}]({repo}/problems/{topic.lower().replace(' ', '_')})"
        summary_table += f"| {topic_link:<19} | {count:<18} |\n"
        total_problems += count

    # Add total row
    summary_table += "|---------------------|--------------------|\n"
    summary_table += f"| **Total**          | **{total_problems}**           |\n"

    return summary_table


def generate_topic_tables(metadata: dict) -> str:
    """Generate separate tables for each topic."""
    repo = metadata["repo"]
    problems = metadata["problems"]
    topic_tables = ""

    difficulty_rank = {"easy": 1, "medium": 2, "hard": 3, "very hard": 4}

    # Group problems by topic
    grouped_problems = {}
    for problem in problems:
        topic = problem["topic"].capitalize()
        grouped_problems.setdefault(topic, []).append(problem)

    # Generate a table for each topic
    for topic, problems in grouped_problems.items():

        sorted_problems = sorted(
            problems,
            key=lambda p: difficulty_rank.get(
                p.get("difficulty").lower(), float("inf")
            ),
        )

        topic_tables += f"### {topic} Problems\n"
        topic_tables += (
            "| #   | Problem               | Difficulty | Languages               |\n"
        )
        topic_tables += (
            "|-----|-----------------------|------------|-------------------------|\n"
        )

        for index, problem in enumerate(sorted_problems, start=1):
            problem_name = problem["name"].replace("_", " ").title()
            problem_url = f"{repo}/{problem['path']}"

            language_links = [
                f"[{lang.capitalize()}]({problem_url}/{lang})"
                for lang in problem["languages"]
            ]

            topic_tables += (
                f"| {index:<3} "
                f"| [{problem_name}]({problem_url}) "
                f"| {problem['difficulty'].capitalize()} "
                f"| {', '.join(language_links)} |\n"
            )

        topic_tables += "\n"  # Add spacing between tables

    return topic_tables


def update_readme(metadata_file: str, readme_file: str) -> None:
    with open(metadata_file, "r") as file:
        metadata = json.load(file)

    summary = generate_summary(metadata)
    topic_tables = generate_topic_tables(metadata)

    with open(readme_file, "r") as file:
        readme = file.readlines()

    start_marker = "<!-- START_TABLE -->\n"
    end_marker = "<!-- END_TABLE -->\n"
    start_index = readme.index(start_marker) + 1
    end_index = readme.index(end_marker)

    # Update the README content
    updated_readme = (
        readme[:start_index]
        + ["## Summary of Problems\n\n", summary, "\n", topic_tables]
        + readme[end_index:]
    )

    with open(readme_file, "w") as file:
        file.writelines(updated_readme)


if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))

    project_root = os.path.abspath(os.path.join(script_dir, ".."))

    metadata_file = os.path.join(project_root, "metadata.json")
    readme_file = os.path.join(project_root, "README.md")

    update_readme(metadata_file, readme_file)
