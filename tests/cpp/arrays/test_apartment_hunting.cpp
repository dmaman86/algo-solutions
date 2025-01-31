#include "../../../problems/arrays/apartment_hunting/cpp/apartment_hunting.h"
#include "../jsontestbase.h"

#include <nlohmann/json.hpp>
#include <unordered_map>
#include <vector>

using json = nlohmann::json;

class ApartmentHuntingTest : public JsonTestBase {
public:
  ApartmentHuntingTest() {
    json_file_path =
        std::string(TEST_CASES_DIR) + "/arrays/apartment_hunting.json";
  }
};

std::vector<std::unordered_map<std::string, bool>>
parseJsonToBlocks(const json &jsonData) {
  std::vector<std::unordered_map<std::string, bool>> blocks;

  for (const auto &block : jsonData) {
    std::unordered_map<std::string, bool> blockMap;
    for (auto it = block.begin(); it != block.end(); it++) {
      blockMap[it.key()] = it.value().get<bool>();
    }
    blocks.push_back(blockMap);
  }
  return blocks;
}

TEST_F(ApartmentHuntingTest, TestCases) {
  ASSERT_FALSE(test_cases.empty()) << "Test cases are empty or not loaded";

  for (const auto &test : test_cases) {
    auto blocks = parseJsonToBlocks(test["blocks"]);
    auto reqs = test["reqs"].get<std::vector<std::string>>();

    auto expected = test["expected"].get<int>();

    auto result = apartmentHunting(blocks, reqs);

    EXPECT_EQ(result, expected) << "Failed for test case: " << test.dump(2);
  }
}
