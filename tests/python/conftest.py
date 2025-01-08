import sys
from pathlib import Path

import pytest


def pytest_addoption(parser):
    parser.addoption(
        "--visualize",
        action="store_true",
        default=False,
        help="Visualize the test cases",
    )


@pytest.fixture
def visualize(request):
    value = request.config.getoption("--visualize")
    print(f"Visualize option from pytest: {value}")
    return value


def pytest_configure():
    root_dir = Path(__file__).resolve().parents[2]
    test_dir = root_dir / "tests" / "python"
    sys.path.append(str(root_dir))
    sys.path.append(str(test_dir))
