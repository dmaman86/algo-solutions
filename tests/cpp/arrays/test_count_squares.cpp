#include "../../../problems/arrays/count_squares/cpp/count_squares.h"
#include "../jsontestbase.h"

#include <vector>

class CountSquaresTest : public JsonTestBase {
public:
  CountSquaresTest() {
    json_file_path = std::string(TEST_CASES_DIR) + "/arrays/count_squares.json";
  }
};

TEST_F(CountSquaresTest, TestCases) {
  ASSERT_FALSE(test_cases.empty()) << "Test cases are empty or not loaded";

  for (const auto &test : test_cases) {
    auto points = test["points"].get<std::vector<std::vector<int>>>();
    int expected = test["expected"].get<int>();

    auto result = countSquares(points);

    EXPECT_EQ(result, expected) << "Test case failed : " << test.dump(2);
  }
}
