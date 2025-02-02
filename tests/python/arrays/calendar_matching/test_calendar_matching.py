from problems.arrays.calendar_matching.python.calendar_matching import \
    calendarMatching
from tests.python.utility import load_test_cases


def test_calendar_matching() -> None:
    test_cases = load_test_cases("arrays/calendar_matching.json")

    for idx, test in enumerate(test_cases):
        calendar1: list[list[str]] = test["calendar1"]
        dailyBounds1: list[str] = test["dailyBounds1"]
        calendar2: list[list[str]] = test["calendar2"]
        dailyBounds2: list[str] = test["dailyBounds2"]
        meetingDuration: int = test["meetingDuration"]

        expected: list[list[str]] = test["expected"]
        result: list[list[str]] = calendarMatching(
            calendar1, dailyBounds1, calendar2, dailyBounds2, meetingDuration
        )

        assert (
            result == expected
        ), f"Test case {idx} failed: expected {expected}, got {result}"
