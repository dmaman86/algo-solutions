#include "../../../problems/graphs/cycle_in_graph/cpp/cycle_in_graph.h"
#include "../jsontestbase.h"

#include <vector>

class TestCycleInGraph : public JsonTestBase {
public:
  TestCycleInGraph() {
    json_file_path =
        std::string(TEST_CASES_DIR) + "/graphs/cycle_in_graph.json";
  }
};

TEST_F(TestCycleInGraph, TestCases) {
  ASSERT_FALSE(test_cases.empty()) << "Test cases are empty!";

  for (const auto &test : test_cases) {
    auto edges = test["edges"].get<std::vector<std::vector<int>>>();
    auto expected = test["expected"].get<bool>();

    auto result = cycleInGraph(edges);

    EXPECT_EQ(result, expected)
        << "Failed test case at index: " << test.dump(2);
  }
}
