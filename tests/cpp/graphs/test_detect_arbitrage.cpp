#include "../../../problems/graphs/detect_arbitrage/cpp/detect_arbitrage.h"
#include "../jsontestbase.h"

#include <vector>

class DetectArbitrageTest : public JsonTestBase {
public:
  DetectArbitrageTest() {
    json_file_path =
        std::string(TEST_CASES_DIR) + "/graphs/detect_arbitrage.json";
  }
};

TEST_F(DetectArbitrageTest, TestCases) {
  ASSERT_FALSE(test_cases.empty()) << "Test cases are empty";

  for (const auto &test : test_cases) {
    auto exchange_rates =
        test["exchangeRates"].get<std::vector<std::vector<double>>>();
    auto expected = test["expected"].get<bool>();

    auto result = detectArbitrage(exchange_rates);

    EXPECT_EQ(result, expected)
        << "Failed test case at index: " << test.dump(2);
  }
}
