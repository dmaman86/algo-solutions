#include "../../../problems/greedy_algorithms/class_photos/cpp/class_photos.h"
#include "../jsontestbase.h"

#include <vector>

class ClassPhotosTest : public JsonTestBase {
public:
  ClassPhotosTest() {
    json_file_path =
        std::string(TEST_CASES_DIR) + "/greedy_algorithms/class_photos.json";
  }
};

TEST_F(ClassPhotosTest, TestCases) {
  ASSERT_FALSE(test_cases.empty()) << "Test cases are empty or not loaded";

  for (const auto &test : test_cases) {
    auto redShirtHeights = test["redShirtHeights"].get<std::vector<int>>();
    auto blueShirtHeights = test["blueShirtHeights"].get<std::vector<int>>();
    bool expected = test["expected"].get<bool>();

    auto result = classPhotos(redShirtHeights, blueShirtHeights);

    EXPECT_EQ(expected, result) << "Failed for test case: " << test.dump(2);
  }
}
