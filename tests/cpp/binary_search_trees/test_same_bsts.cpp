#include "../../../problems/binary_search_trees/same_bsts/cpp/same_bsts.h"
#include "../jsontestbase.h"

#include <vector>

class TestSameBSTs : public JsonTestBase {
public:
  TestSameBSTs() {
    json_file_path =
        std::string(TEST_CASES_DIR) + "/binary_search_trees/same_bsts.json";
  }
};

TEST_F(TestSameBSTs, TestCases) {
  ASSERT_FALSE(test_cases.empty()) << "Test cases are empty";

  for (const auto &test : test_cases) {
    auto arrayOne = test["arrayOne"].get<std::vector<int>>();
    auto arrayTwo = test["arrayTwo"].get<std::vector<int>>();
    auto expected = test["expected"].get<bool>();

    auto result = sameBsts(arrayOne, arrayTwo);

    EXPECT_EQ(result, expected) << "Failed for test: " << test.dump(2);
  }
}
