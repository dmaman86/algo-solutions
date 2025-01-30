#include "../../../problems/greedy_algorithms/valid_starting_city/cpp/valid_starting_city.h"
#include "../jsontestbase.h"

#include <vector>

class ValidStartingCityTest : public JsonTestBase {
public:
  ValidStartingCityTest() {
    json_file_path = std::string(TEST_CASES_DIR) +
                     "/greedy_algorithms/valid_starting_city.json";
  }
};

TEST_F(ValidStartingCityTest, TestCases) {
  ASSERT_FALSE(test_cases.empty()) << "Test cases are empty or not loaded";

  for (const auto &test : test_cases) {
    auto distances = test["distances"].get<std::vector<int>>();
    auto fuel = test["fuel"].get<std::vector<int>>();
    auto mpg = test["mpg"].get<int>();

    auto expected = test["expected"].get<int>();

    auto result = validStartingCity(distances, fuel, mpg);

    EXPECT_EQ(result, expected) << "Failed for test case: " << test.dump(2);
  }
}
