#include <vector>

struct StringMeeting {
  std::string start;
  std::string end;

  bool operator==(const StringMeeting &other) const {
    return start == other.start && end == other.end;
  }
};

std::vector<StringMeeting> calendarMatching(std::vector<StringMeeting>,
                                            StringMeeting,
                                            std::vector<StringMeeting>,
                                            StringMeeting, int);
