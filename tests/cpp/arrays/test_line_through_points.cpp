#include "../../../problems/arrays/line_through_points/cpp/line_through_points.h"
#include "../jsontestbase.h"

#include <vector>

class LineThroughPointsTest : public JsonTestBase {
public:
  LineThroughPointsTest() {
    json_file_path =
        std::string(TEST_CASES_DIR) + "/arrays/line_through_points.json";
  }
};

TEST_F(LineThroughPointsTest, TestCases) {
  ASSERT_FALSE(test_cases.empty()) << "Test cases are empty or not loaded";

  for (const auto &test : test_cases) {
    auto points = test["points"].get<std::vector<std::vector<int>>>();
    auto expected = test["expected"].get<int>();

    auto result = lineThroughPoints(points);

    EXPECT_EQ(result, expected) << "Failed on test case: " << test.dump(2);
  }
}
