#include "../../../problems/famous_algorithms/dijkstras_algorithm/cpp/dijkstras_algorithm.h"
#include <filesystem>
#include <fstream>
#include <gtest/gtest.h>
#include <iostream>
#include <nlohmann/json.hpp>
#include <vector>

using json = nlohmann::json;

typedef std::vector<std::vector<int>> twod_vector;
typedef std::vector<twod_vector> threed_vector;

class DijkstrasAlgorithmTest : public ::testing::Test {
protected:
  void SetUp() override {
    std::string test_file = std::string(TEST_CASES_DIR) +
                            "/famous_algorithms/dijkstras_algorithm.json";
    std::ifstream f(test_file);

    if (!f.is_open())
      throw std::runtime_error("Could not open file: " + test_file);

    test_cases = json::parse(f);
  }
  json test_cases;
};

TEST_F(DijkstrasAlgorithmTest, TestCases) {

  for (auto &test : test_cases) {
    int start = test["start"];
    threed_vector edges = test["edges"];
    std::vector<int> expected = test["expected"];

    std::vector<int> result = dijkstrasAlgorithm(start, edges);

    // std::cout << "Start: " << start << "\n";
    // std::cout << "Edges: ";
    // for (const auto &node : edges) {
    //   std::cout << "[";
    //   for (const auto &edge : node) {
    //     std::cout << "[";
    //     for (const auto &value : edge) {
    //       std::cout << value << " ";
    //     }
    //     std::cout << "]";
    //   }
    //   std::cout << "]";
    // }
    // std::cout << "\n";
    // std::cout << "Expected: ";
    // for (const auto &val : expected) {
    //   std::cout << val << " ";
    // }
    // std::cout << "\n";
    // std::cout << "Result: ";
    // for (const auto &val : result) {
    //   std::cout << val << " ";
    // }
    // std::cout << "\n";

    EXPECT_EQ(result, expected) << "Failed for test case: " << test.dump(2);
  }
}
