#include "../../../problems/famous_algorithms/astar_algorithm/cpp/astar_algorithm.h"
#include <fstream>
#include <gtest/gtest.h>
#include <nlohmann/json.hpp>
#include <vector>

using json = nlohmann::json;

class AStarAlgorithmTest : public ::testing::Test {
protected:
  void SetUp() override {
    std::string test_file =
        std::string(TEST_CASES_DIR) + "/famous_algorithms/astar_algorithm.json";
    std::ifstream f(test_file);

    if (!f.is_open()) {
      throw std::runtime_error("Failed to open test file: " + test_file);
    }
    test_cases = json::parse(f);
  }
  json test_cases;
};

TEST_F(AStarAlgorithmTest, TestCases) {

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
