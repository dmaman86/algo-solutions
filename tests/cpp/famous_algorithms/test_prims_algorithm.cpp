#include "../../../problems/famous_algorithms/prims_algorithm/cpp/prims_algorithm.h"
#include "../jsontestbase.h"

#include <vector>

using AdjacencyList = std::vector<std::vector<std::vector<int>>>;

class PrimsAlgorithmTest : public JsonTestBase {
public:
  PrimsAlgorithmTest() {
    json_file_path =
        std::string(TEST_CASES_DIR) + "/famous_algorithms/prims_algorithm.json";
  }
};

TEST_F(PrimsAlgorithmTest, TestCases) {
  ASSERT_FALSE(test_cases.empty()) << "Test cases are empty";
  for (const auto &test : test_cases) {
    auto edges = test["edges"].get<AdjacencyList>();

    auto expected = test["expected"].get<AdjacencyList>();
    auto result = primsAlgorithm(edges);

    EXPECT_EQ(result, expected)
        << "Test failed for test cases: " << test.dump(2);
  }
}
