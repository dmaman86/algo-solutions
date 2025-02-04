#include "../../../problems/arrays/subarray_sort/cpp/subarray_sort.h"
#include "../jsontestbase.h"

#include <vector>

class SubarraySortTest : public JsonTestBase {
public:
  SubarraySortTest() {
    json_file_path = std::string(TEST_CASES_DIR) + "/arrays/subarray_sort.json";
  }
};

TEST_F(SubarraySortTest, TestCases) {
  ASSERT_FALSE(test_cases.empty()) << "Test cases are empty";
  for (const auto &test : test_cases) {
    auto array = test["array"].get<std::vector<int>>();
    auto expected = test["expected"].get<std::vector<int>>();

    auto result = subarraySort(array);

    EXPECT_EQ(result, expected) << "Failed for test cases: " << test.dump(2);
  }
}
