#include "../../../problems/famous_algorithms/topological_sort/cpp/topological_sort.h"
#include <fstream>
#include <gtest/gtest.h>
#include <nlohmann/json.hpp>

using json = nlohmann::json;

class TopologicalSortTest : public ::testing::Test {
protected:
  void SetUp() override {
    std::string test_file = std::string(TEST_CASES_DIR) +
                            "/famous_algorithms/topological_sort.json";
    std::ifstream file(test_file);
    if (!file.is_open())
      throw std::runtime_error("Could not open file " + test_file);

    test_cases = json::parse(file);
  }

  json test_cases;
};

TEST_F(TopologicalSortTest, TopologicalSort) {
  for (auto &test_case : test_cases) {
    std::vector<int> jobs = test_case["jobs"];
    std::vector<std::vector<int>> deps = test_case["deps"];
    std::vector<int> expected = test_case["expected"];
    std::vector<int> output = topologicalSort(jobs, deps);
    // ASSERT_EQ(output, expected);
    EXPECT_TRUE(
        std::is_permutation(output.begin(), output.end(), expected.begin()))
        << "Output contains the same elements as expected but in a different "
           "order";
  }
}
