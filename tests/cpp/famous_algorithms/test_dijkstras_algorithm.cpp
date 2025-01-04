#include "../../../problems/famous_algorithms/dijkstras_algorithm/cpp/dijkstras_algorithm.h"
#include "../jsontestbase.h"

#include <gtest/gtest.h>

#include <nlohmann/json.hpp>
#include <vector>

using json = nlohmann::json;

typedef std::vector<std::vector<int>> twod_vector;
typedef std::vector<twod_vector> threed_vector;

class DijkstrasAlgorithmTest : public JsonTestBase {
public:
  DijkstrasAlgorithmTest() {
    json_file_path = std::string(TEST_CASES_DIR) +
                     "/famous_algorithms/dijkstras_algorithm.json";
  }
};

TEST_F(DijkstrasAlgorithmTest, TestCases) {
  ASSERT_FALSE(test_cases.empty()) << "Test cases are empty";
  for (auto &test : test_cases) {
    int start = test["start"];
    threed_vector edges = test["edges"];
    std::vector<int> expected = test["expected"];

    std::vector<int> result = dijkstrasAlgorithm(start, edges);

    EXPECT_EQ(result, expected) << "Failed for test case: " << test.dump(2);
  }
}
