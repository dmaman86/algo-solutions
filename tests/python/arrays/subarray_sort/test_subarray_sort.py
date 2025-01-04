from subarray_sort.python.subarray_sort import subarray_sort
from utility import load_test_cases


def test_subarray_sort() -> None:
    test_cases = load_test_cases("arrays/subarray_sort.json")

    for idx, test in enumerate(test_cases):
        array = test["array"]
        expected = test["expected"]
        result = subarray_sort(array)

        assert result == expected, f"Test case failed ar index {idx}"
