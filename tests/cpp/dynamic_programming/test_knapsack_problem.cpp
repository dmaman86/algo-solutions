#include "../../../problems/dynamic_programming/knapsack_problem/cpp/knapsack_problem.h"
#include "../jsontestbase.h"

#include <algorithm>
#include <nlohmann/json.hpp>
#include <utility>
#include <vector>

using json = nlohmann::json;
using ExpectedResult = std::pair<int, std::vector<int>>;

class KnapsackProblemTest : public JsonTestBase {
public:
  KnapsackProblemTest() {
    json_file_path = std::string(TEST_CASES_DIR) +
                     "/dynamic_programming/knapsack_problem.json";
  }
};

ExpectedResult parseExpected(const json &expected) {
  int totalValue = expected[0].get<int>();
  std::vector<int> selectedItems = expected[1].get<std::vector<int>>();
  return {totalValue, selectedItems};
}

bool arePermutations(const std::vector<int> &vec1,
                     const std::vector<int> &vec2) {
  if (vec1.size() != vec2.size())
    return false;

  std::vector<int> sorted_vec1 = vec1;
  std::vector<int> sorted_vec2 = vec2;

  std::sort(sorted_vec1.begin(), sorted_vec1.end());
  std::sort(sorted_vec2.begin(), sorted_vec2.end());

  return sorted_vec1 == sorted_vec2;
}

TEST_F(KnapsackProblemTest, TestCases) {
  ASSERT_FALSE(test_cases.empty()) << "Test cases are empty";

  for (const auto &test : test_cases) {
    auto items = test["items"].get<vector2DInt>();
    auto capacity = test["capacity"].get<int>();
    auto expected = parseExpected(test["expected"]);

    auto result = knapsackProblem(items, capacity);

    ASSERT_EQ(result[0][0], expected.first) << "Total value is different";

    EXPECT_TRUE(arePermutations(result[1], expected.second))
        << "Items are different for test: " << test.dump(2);
  }
}
