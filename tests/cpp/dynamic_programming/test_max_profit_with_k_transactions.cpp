#include "../../../problems/dynamic_programming/max_profit_with_k_transactions/cpp/max_profit_with_k_transactions.h"
#include "../jsontestbase.h"

#include <vector>

class MaxProfitWithKTransactionsTest : public JsonTestBase {
public:
  MaxProfitWithKTransactionsTest() {
    json_file_path = std::string(TEST_CASES_DIR) +
                     "/dynamic_programming/max_profit_with_k_transactions.json";
  }
};

TEST_F(MaxProfitWithKTransactionsTest, TestCases) {
  ASSERT_FALSE(test_cases.empty()) << "Test cases are empty";

  for (const auto &test : test_cases) {
    auto prices = test["prices"].get<std::vector<int>>();
    int k = test["k"].get<int>();
    int expected = test["expected"].get<int>();

    auto result = maxProfitWithKTransactions(prices, k);

    EXPECT_EQ(result, expected) << "Failed test case: " << test.dump(2);
  }
}
