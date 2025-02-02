#include "../../../problems/arrays/calendar_matching/cpp/calendar_matching.h"
#include "../jsontestbase.h"

#include <nlohmann/json.hpp>
#include <vector>

using json = nlohmann::json;

class CalendarMatchingTest : public JsonTestBase {
public:
  CalendarMatchingTest() {
    json_file_path =
        std::string(TEST_CASES_DIR) + "/arrays/calendar_matching.json";
  }
};

std::vector<StringMeeting> parseCalendar(const json &calendarJson) {
  std::vector<StringMeeting> calendar;

  for (const auto &meeting : calendarJson) {
    calendar.push_back({meeting[0], meeting[1]});
  }
  return calendar;
}

TEST_F(CalendarMatchingTest, TestCases) {
  ASSERT_FALSE(test_cases.empty()) << "Test cases are empty or not loaded";

  for (const auto &test : test_cases) {
    auto calendar1 = parseCalendar(test["calendar1"]);
    StringMeeting dailyBounds1 = {test["dailyBounds1"][0],
                                  test["dailyBounds1"][1]};
    auto calendar2 = parseCalendar(test["calendar2"]);
    StringMeeting dailyBounds2 = {test["dailyBounds2"][0],
                                  test["dailyBounds2"][1]};
    int meetingDuration = test["meetingDuration"];

    auto expected = parseCalendar(test["expected"]);

    auto result = calendarMatching(calendar1, dailyBounds1, calendar2,
                                   dailyBounds2, meetingDuration);

    EXPECT_EQ(result, expected) << "Failed test case: " << test.dump(2);
  }
}
