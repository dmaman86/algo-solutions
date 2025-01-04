#include "../../../problems/famous_algorithms/astar_algorithm/cpp/astar_algorithm.h"
#include "../jsontestbase.h"
#include <gtest/gtest.h>
#include <nlohmann/json.hpp>
#include <vector>

using json = nlohmann::json;

class AStarAlgorithmTest : public JsonTestBase {
public:
  AStarAlgorithmTest() {
    json_file_path =
        std::string(TEST_CASES_DIR) + "/famous_algorithms/astar_algorithm.json";
  }
};

TEST_F(AStarAlgorithmTest, TestCases) {
  ASSERT_FALSE(test_cases.empty()) << "Test cases are empty";
  for (const auto &test : test_cases) {
    auto startRow = test["startRow"].get<int>();
    auto startCol = test["startCol"].get<int>();
    auto endRow = test["endRow"].get<int>();
    auto endCol = test["endCol"].get<int>();
    auto graph = test["graph"].get<std::vector<std::vector<int>>>();

    auto expected = test["expected"].get<std::vector<std::vector<int>>>();
    auto result = aStarAlgorithm(startRow, startCol, endRow, endCol, graph);

    ASSERT_EQ(result, expected) << "Failed for test case: " << test.dump(2);
  }
}
