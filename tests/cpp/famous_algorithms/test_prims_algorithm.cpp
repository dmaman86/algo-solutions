#include "../../../problems/famous_algorithms/prims_algorithm/cpp/prims_algorithm.h"
#include <algorithm>
#include <fstream>
#include <gtest/gtest.h>
#include <nlohmann/json.hpp>
#include <vector>

using json = nlohmann::json;
using AdjacencyList = std::vector<std::vector<std::vector<int>>>;

class PrimsAlgorithmTest : public ::testing::Test {
protected:
  void SetUp() override {
    std::string file_path =
        std::string(TEST_CASES_DIR) + "/famous_algorithms/prims_algorithm.json";
    std::ifstream file(file_path);
    if (!file.is_open())
      throw std::runtime_error("Could not open file");
    test_cases = json::parse(file);
  }
  json test_cases;
};

TEST_F(PrimsAlgorithmTest, TestCases) {
  for (const auto &test : test_cases) {
    auto edges = test["edges"].get<AdjacencyList>();

    auto expected = test["expected"].get<AdjacencyList>();
    auto result = primsAlgorithm(edges);

    EXPECT_EQ(result, expected)
        << "Test failed for test cases: " << test.dump(2);
  }
}
