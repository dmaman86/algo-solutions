from problems.greedy_algorithms.class_photos.python.class_photos import \
    classPhotos
from tests.python.utility import load_test_cases


def test_class_photos() -> None:
    test_cases = load_test_cases("greedy_algorithms/class_photos.json")

    for idx, test in enumerate(test_cases):
        redShirtHeights: list[int] = test["redShirtHeights"]
        blueShirtHeights: list[int] = test["blueShirtHeights"]
        expected: bool = test["expected"]

        result: bool = classPhotos(redShirtHeights, blueShirtHeights)
        assert (
            result == expected
        ), f"Test case {idx} failed: expected {expected}, got {result}"
