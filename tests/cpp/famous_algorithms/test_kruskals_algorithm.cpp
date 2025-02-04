#include "../../../problems/famous_algorithms/kruskals_algorithm/cpp/kruskals_algorithm.h"
#include "../jsontestbase.h"

#include <vector>

class KruskalsAlgorithmTest : public JsonTestBase {
public:
  KruskalsAlgorithmTest() {
    json_file_path = std::string(TEST_CASES_DIR) +
                     "/famous_algorithms/kruskals_algorithm.json";
  }
};

TEST_F(KruskalsAlgorithmTest, TestCases) {
  ASSERT_FALSE(test_cases.empty()) << "Test cases are empty";
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
