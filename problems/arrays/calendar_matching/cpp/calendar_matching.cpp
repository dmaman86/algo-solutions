#include "calendar_matching.h"

#include <algorithm>
#include <sstream>

std::vector<StringMeeting>
calendarMatching(std::vector<StringMeeting> calendar1,
                 StringMeeting dailyBounds1,
                 std::vector<StringMeeting> calendar2,
                 StringMeeting dailyBounds2, int meetingDuration) {

  auto timeToMinutes = [](const std::string &time) -> int {
    int hours, minutes;
    char delimiter;
    std::stringstream ss(time);
    ss >> hours >> delimiter >> minutes;
    return hours * 60 + minutes;
  };

  auto minutesToTime = [](int minutes) -> std::string {
    int hours = minutes / 60;
    int mins = minutes % 60;
    return std::to_string(hours) + ":" + (mins < 10 ? "0" : "") +
           std::to_string(mins);
  };

  auto updateCalendar =
      [&](const std::vector<StringMeeting> &calendar,
          const StringMeeting &dailyBounds) -> std::vector<std::vector<int>> {
    int start = timeToMinutes(dailyBounds.start);
    int end = timeToMinutes(dailyBounds.end);
    const int END_OF_DAY = 1440;

    std::vector<std::vector<int>> filteredCalendar;
    filteredCalendar.reserve(calendar.size() + 2);

    filteredCalendar.push_back({0, start});

    for (const auto &meeting : calendar) {
      std::vector<int> timeSlot = {timeToMinutes(meeting.start),
                                   timeToMinutes(meeting.end)};
      if (timeSlot[1] > start && timeSlot[0] < end) {
        filteredCalendar.push_back(timeSlot);
      }
    }
    filteredCalendar.push_back({end, END_OF_DAY});
    return filteredCalendar;
  };

  auto mergeCalendars = [&](const std::vector<std::vector<int>> &calendar1,
                            const std::vector<std::vector<int>> &calendar2)
      -> std::vector<std::vector<int>> {
    std::vector<std::vector<int>> merged;
    merged.reserve(calendar1.size() + calendar2.size());

    int i = 0, j = 0;
    std::vector<int> last = {-1, -1};

    while (i < calendar1.size() || j < calendar2.size()) {
      std::vector<int> meeting;
      if (j >= calendar2.size() ||
          (i < calendar1.size() && calendar1[i][0] < calendar2[j][0])) {
        meeting = calendar1[i++];
      } else {
        meeting = calendar2[j++];
      }

      if (last[1] >= meeting[0]) {
        last[1] = std::max(last[1], meeting[1]); // Merge overlapping intervals
      } else {
        if (last[0] != -1)
          merged.push_back(last);
        last = meeting;
      }
    }
    if (last[0] != -1)
      merged.push_back(last);
    return merged;
  };

  auto findAvailableTimes = [&](const std::vector<std::vector<int>> &calendar)
      -> std::vector<StringMeeting> {
    std::vector<StringMeeting> available;
    available.reserve(calendar.size());

    for (size_t i = 1; i < calendar.size(); i++) {
      int previousEnd = calendar[i - 1][1];
      int currentStart = calendar[i][0];
      if (currentStart - previousEnd >= meetingDuration) {
        available.push_back(
            {minutesToTime(previousEnd), minutesToTime(currentStart)});
      }
    }

    return available;
  };

  auto updatedCalendar1 = updateCalendar(calendar1, dailyBounds1);
  auto updatedCalendar2 = updateCalendar(calendar2, dailyBounds2);
  auto mergedCalendar = mergeCalendars(updatedCalendar1, updatedCalendar2);

  return findAvailableTimes(mergedCalendar);
}
