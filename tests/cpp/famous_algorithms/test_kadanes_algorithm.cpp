#include "../../../problems/famous_algorithms/kadanes_algorithm/cpp/kadanes_algorithm.h"
#include "../jsontestbase.h"
#include <gtest/gtest.h>
#include <nlohmann/json.hpp>

using json = nlohmann::json;

class KadanesAlgorithmTest : public JsonTestBase {
public:
  KadanesAlgorithmTest() {
    json_file_path = std::string(TEST_CASES_DIR) +
                     "/famous_algorithms/kadanes_algorithm.json";
  }
};

TEST_F(KadanesAlgorithmTest, TestCases) {
  ASSERT_FALSE(test_cases.empty()) << "Test cases are empty";
  for (auto &test : test_cases) {
    std::vector<int> array = test["array"];
    int expected = test["expected"];
    int actual = kadanesAlgorithm(array);
    EXPECT_EQ(expected, actual) << "Failed on test case: " << test.dump(2);
  }
}
