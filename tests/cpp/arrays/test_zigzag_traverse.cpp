#include "../../../problems/arrays/zigzag_traverse/cpp/zigzag_traverse.h"
#include "../jsontestbase.h"

#include <vector>

class ZigzagTraverseTest : public JsonTestBase {
public:
  ZigzagTraverseTest() {
    json_file_path =
        std::string(TEST_CASES_DIR) + "/arrays/zigzag_traverse.json";
  }
};

TEST_F(ZigzagTraverseTest, TestCases) {
  ASSERT_FALSE(test_cases.empty()) << "Test cases are empty or not loaded";

  for (const auto &test : test_cases) {
    auto array = test["array"].get<std::vector<std::vector<int>>>();
    auto expected = test["expected"].get<std::vector<int>>();

    auto result = zigzagTraverse(array);

    EXPECT_EQ(result, expected) << "Failed for test case: " << test.dump(2);
  }
}
