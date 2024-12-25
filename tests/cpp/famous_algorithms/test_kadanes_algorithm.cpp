#include "../../../problems/famous_algorithms/kadanes_algorithm/cpp/kadanes_algorithm.h"
#include <filesystem>
#include <fstream>
#include <gtest/gtest.h>
#include <nlohmann/json.hpp>

using json = nlohmann::json;

class KadanesAlgorithmTest : public ::testing::Test {
protected:
  void SetUp() override {
    std::string test_file = std::string(TEST_CASES_DIR) +
                            "/famous_algorithms/kadanes_algorithm.json";
    std::ifstream f(test_file);
    if (!f.is_open()) {
      throw std::runtime_error("Couldn't open test file: " + test_file);
    }
    test_cases = json::parse(f);
  }
  json test_cases;
};

TEST_F(KadanesAlgorithmTest, TestCases) {
  for (auto &test : test_cases) {
    std::vector<int> array = test["array"];
    int expected = test["expected"];
    int actual = kadanesAlgorithm(array);
    EXPECT_EQ(expected, actual) << "Failed on test case: " << test.dump(2);
  }
}
