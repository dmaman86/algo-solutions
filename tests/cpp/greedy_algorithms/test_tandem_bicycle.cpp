#include "../../../problems/greedy_algorithms/tandem_bicycle/cpp/tandem_bicycle.h"
#include "../jsontestbase.h"

#include <vector>

class TandemBicycleTest : public JsonTestBase {
public:
  TandemBicycleTest() {
    json_file_path =
        std::string(TEST_CASES_DIR) + "/greedy_algorithms/tandem_bicycle.json";
  }
};

TEST_F(TandemBicycleTest, TestCases) {
  ASSERT_FALSE(test_cases.empty()) << "Test cases are empty or not loeaded";

  for (const auto &test : test_cases) {
    auto redShirtSpeeds = test["redShirtSpeeds"].get<std::vector<int>>();
    auto blueShirtSpeeds = test["blueShirtSpeeds"].get<std::vector<int>>();
    bool fastest = test["fastest"].get<bool>();

    int expected = test["expected"].get<int>();
    int result = tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest);

    EXPECT_EQ(result, expected) << "Failed for test case: " << test.dump(2);
  }
}
