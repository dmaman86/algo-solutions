#include "../../../problems/arrays/min_rewards/cpp/min_rewards.h"
#include "../jsontestbase.h"

#include <vector>

class TestMinRewards : public JsonTestBase {
public:
  TestMinRewards() {
    json_file_path = std::string(TEST_CASES_DIR) + "/arrays/min_rewards.json";
  }
};

TEST_F(TestMinRewards, TestCases) {
  ASSERT_FALSE(test_cases.empty()) << "Test cases are empty or not loaded";

  for (const auto &test : test_cases) {
    auto scores = test["scores"].get<std::vector<int>>();
    auto expected = test["expected"].get<int>();

    auto result = minRewards(scores);

    EXPECT_EQ(result, expected) << "Failed for test case: " << test.dump(2);
  }
}
