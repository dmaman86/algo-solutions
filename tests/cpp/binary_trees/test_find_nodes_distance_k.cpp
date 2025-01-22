#include "../../../problems/binary_trees/find_nodes_distance_k/cpp/find_nodes_distance_k.h"
#include "../jsontestbase.h"
#include "./utility.h"

#include <algorithm>
#include <vector>

class FindNodesDistanceKTest : public JsonTestBase {
public:
  FindNodesDistanceKTest() {
    json_file_path = std::string(TEST_CASES_DIR) +
                     "/binary_trees/find_nodes_distance_k.json";
  }
};

TEST_F(FindNodesDistanceKTest, TestCases) {
  ASSERT_FALSE(test_cases.empty()) << "Test cases are empty";

  for (const auto &test : test_cases) {
    auto treeJson = test["tree"];
    auto target = test["target"].get<int>();
    auto k = test["k"].get<int>();
    auto expected = test["expected"].get<std::vector<int>>();

    auto root = buildBT(treeJson);
    auto result = findNodesDistanceK(root, target, k);

    std::sort(result.begin(), result.end());
    std::sort(expected.begin(), expected.end());

    EXPECT_EQ(result, expected) << "Failed for test case: " << test.dump(2);

    deleteBT(root);
  }
}
