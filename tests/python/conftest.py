import sys
from pathlib import Path


def pytest_configure():
    root_dir = Path(__file__).resolve().parents[2]
    problems_dir = root_dir / "problems"
    test_dir = root_dir / "tests" / "python"

    sys.path.append(str(test_dir))

    problem_categories = [
        "arrays",
        "famous_algorithms",
        "graphs",
        "binary_search_trees",
    ]

    for category in problem_categories:
        category_path = problems_dir / category
        if category_path.exists():
            sys.path.append(str(category_path))
