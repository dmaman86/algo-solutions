#include "../../../problems/famous_algorithms/kruskals_algorithm/cpp/kruskals_algorithm.h"
#include <fstream>
#include <gtest/gtest.h>
#include <nlohmann/json.hpp>
#include <vector>

using json = nlohmann::json;

class KruskalsAlgorithmTest : public ::testing::Test {
protected:
  void SetUp() override {
    std::string file_path = std::string(TEST_CASES_DIR) +
                            "/famous_algorithms/kruskals_algorithm.json";
    std::ifstream f(file_path);

    if (!f.is_open()) {
      throw std::runtime_error("Failed to open file");
    }
    test_cases = json::parse(f);
  }
  json test_cases;
};

TEST_F(KruskalsAlgorithmTest, TestCases) {
  for (const auto &test : test_cases) {
    auto edges =
        test["edges"].get<std::vector<std::vector<std::vector<int>>>>();
    auto expected =
        test["expected"].get<std::vector<std::vector<std::vector<int>>>>();

    auto result = kruskalsAlgorithm(edges);
    EXPECT_EQ(result, expected)
        << "Test failed for test cases: " << test.dump(2);
  }
}
