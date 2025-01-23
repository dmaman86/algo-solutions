#include "../../../problems/binary_search_trees/validate_three_nodes/cpp/validate_three_nodes.h"
#include "../jsontestbase.h"
#include "./utility.h"

#include <sstream>

class ValidateThreeNodesTest : public JsonTestBase {
public:
  ValidateThreeNodesTest() {
    json_file_path = std::string(TEST_CASES_DIR) +
                     "/binary_search_trees/validate_three_nodes.json";
  }
};

BST *findNode(BST *root, int targetValue) {
  if (!root)
    return nullptr;

  if (root->value == targetValue)
    return root;

  BST *nextNode = (targetValue > root->value) ? root->right : root->left;
  return findNode(nextNode, targetValue);
}

int convertToInteger(const std::string &str) {
  std::stringstream ss(str);
  int value;
  ss >> value;
  return value;
}

TEST_F(ValidateThreeNodesTest, TestCases) {
  ASSERT_FALSE(test_cases.empty()) << "Test cases are empty or not loaded";

  for (const auto &test : test_cases) {
    auto treeJson = test["tree"];
    auto nodeOne = convertToInteger(test["nodeOne"]);
    auto nodeTwo = convertToInteger(test["nodeTwo"]);
    auto nodeThree = convertToInteger(test["nodeThree"]);
    auto expected = test["expected"];

    auto root = buildBST(treeJson);
    auto nodeOnePtr = findNode(root, nodeOne);
    auto nodeTwoPtr = findNode(root, nodeTwo);
    auto nodeThreePtr = findNode(root, nodeThree);

    auto result = validateThreeNodes(nodeOnePtr, nodeTwoPtr, nodeThreePtr);

    EXPECT_EQ(result, expected) << "Failed test case " << test.dump(2);

    deleteBST(root);
  }
}
