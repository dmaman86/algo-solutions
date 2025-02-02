import { calendarMatching } from "@/arrays/calendar_matching/js/calendar_matching";
import { expect } from "@jest/globals";

import testCases from "../../test_cases/arrays/calendar_matching.json";

describe("Calendar Matching Test", () => {
  testCases.forEach(
    (
      {
        calendar1,
        dailyBounds1,
        calendar2,
        dailyBounds2,
        meetingDuration,
        expected,
      },
      idx,
    ) => {
      test(`Test case ${idx}`, () => {
        const result = calendarMatching(
          calendar1,
          dailyBounds1,
          calendar2,
          dailyBounds2,
          meetingDuration,
        );

        expect(result).toEqual(expected, `Test case ${idx} failed`);
      });
    },
  );
});
