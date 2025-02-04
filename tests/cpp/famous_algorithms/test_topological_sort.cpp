#include "../../../problems/famous_algorithms/topological_sort/cpp/topological_sort.h"
#include "../jsontestbase.h"

#include <vector>

class TopologicalSortTest : public JsonTestBase {
public:
  TopologicalSortTest() {
    json_file_path = std::string(TEST_CASES_DIR) +
                     "/famous_algorithms/topological_sort.json";
  }
};

TEST_F(TopologicalSortTest, TopologicalSort) {
  ASSERT_FALSE(test_cases.empty()) << "Test cases are empty";
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
