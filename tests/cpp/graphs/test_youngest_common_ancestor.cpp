#include "../../../problems/graphs/youngest_common_ancestor/cpp/youngest_common_ancestor.h"
#include "../jsontestbase.h"

#include <nlohmann/json.hpp>
#include <unordered_map>
#include <vector>

using json = nlohmann::json;

class YoungestCommonAncestorTest : public JsonTestBase {
public:
  YoungestCommonAncestorTest() {
    json_file_path =
        std::string(TEST_CASES_DIR) + "/graphs/youngest_common_ancestor.json";
  }
};

std::unordered_map<char, AncestralTree *> buildMap(const json &treeJson) {
  const auto &nodes = treeJson["nodes"];

  std::unordered_map<char, AncestralTree *> nodeMap;

  for (const auto &node : nodes) {
    char name = node["name"].get<std::string>()[0];
    nodeMap[name] = new AncestralTree(name);
  }

  for (const auto &node : nodes) {
    char name = node["name"].get<std::string>()[0];
    if (!node["ancestor"].is_null()) {
      char ancestorName = node["ancestor"].get<std::string>()[0];
      nodeMap[ancestorName]->addAsAncestor({nodeMap[name]});
    }
  }
  return nodeMap;
}

AncestralTree *
findNode(const std::unordered_map<char, AncestralTree *> &nodeMap,
         char targetName) {
  auto it = nodeMap.find(targetName);
  return (it != nodeMap.end()) ? it->second : nullptr;
}

void clearMap(std::unordered_map<char, AncestralTree *> &nodeMap) {
  for (auto &[name, node] : nodeMap) {
    delete node;
  }
  nodeMap.clear();
}

TEST_F(YoungestCommonAncestorTest, TestCases) {
  ASSERT_FALSE(test_cases.empty()) << "Test cases are empty or not loaded";

  for (const auto &test : test_cases) {
    auto treeJson = test["ancestralTree"];
    auto topAcestorChar = test["topAncestor"].get<std::string>()[0];
    auto descendantOneChar = test["descendantOne"].get<std::string>()[0];
    auto descendantTwoChar = test["descendantTwo"].get<std::string>()[0];

    std::unordered_map<char, AncestralTree *> nodeMap = buildMap(treeJson);

    AncestralTree *topAncestor = findNode(nodeMap, topAcestorChar);
    AncestralTree *descendantOne = findNode(nodeMap, descendantOneChar);
    AncestralTree *descendantTwo = findNode(nodeMap, descendantTwoChar);

    auto expectedJson = test["expected"];

    auto result =
        getYoungestCommonAncestor(topAncestor, descendantOne, descendantTwo);

    EXPECT_EQ(result->name, expectedJson["nodeId"].get<std::string>()[0])
        << "Failed for test case: " << test.dump(2);

    clearMap(nodeMap);
  }
}
