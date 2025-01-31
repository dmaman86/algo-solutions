#include "../../../problems/greedy_algorithms/minimum_waiting_time/cpp/minimum_waiting_time.h"
#include "../jsontestbase.h"

#include <vector>

class MinimumWaitingTimeTest : public JsonTestBase {
public:
  MinimumWaitingTimeTest() {
    json_file_path = std::string(TEST_CASES_DIR) +
                     "/greedy_algorithms/minimum_waiting_time.json";
  }
};

TEST_F(MinimumWaitingTimeTest, TestCases) {
  ASSERT_FALSE(test_cases.empty()) << "Test cases are empty or not loaded";

  for (const auto &test : test_cases) {
    auto queries = test["queries"].get<std::vector<int>>();
    auto expected = test["expected"].get<int>();

    auto result = minimumWaitingTime(queries);

    EXPECT_EQ(result, expected) << "Failed for test case: " << test.dump(2);
  }
}
