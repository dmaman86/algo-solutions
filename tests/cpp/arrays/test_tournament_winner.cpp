#include "../../../problems/arrays/tournament_winner/cpp/tournament_winner.h"
#include <filesystem>
#include <fstream>
#include <gtest/gtest.h>
#include <nlohmann/json.hpp>

using json = nlohmann::json;

class TournamentWinnerTest : public ::testing::Test {
protected:
  void SetUp() override {
    std::string test_file =
        std::string(TEST_CASES_DIR) + "/arrays/tournament_winner.json";
    std::ifstream f(test_file);
    if (!f.is_open()) {
      throw std::runtime_error("Couldn't open test file: " + test_file);
    }
    test_cases = json::parse(f);
  }

  json test_cases;
};

TEST_F(TournamentWinnerTest, TestCases) {
  for (auto &test : test_cases) {
    std::vector<std::vector<std::string>> competitions = test["competitions"];
    std::vector<int> results = test["results"];
    std::string expected = test["expected"];
    std::string actual = tournamentWinner(competitions, results);
    EXPECT_EQ(expected, actual) << "Failed on test case: " << test.dump(2);
  }
}

// TEST(TournamentWinnerTest, JSONCases) {
//
//   const std::string jsonPath =
//   "../../test_cases/arrays/tournament_winner.json";
//
//   std::ifstream file(jsonPath);
//
//   ASSERT_TRUE(file.is_open()) << "Couldn't open test file";
//
//   json testData;
//   file >> testData;
//
//   for (size_t i = 0; i < testData.size(); i++) {
//     auto data = testData[i];
//     std::vector<std::vector<std::string>> competitions =
//     data["competitions"]; std::vector<int> results = data["results"];
//     std::string expected = data["expected"];
//
//     std::string actual = tournamentWinner(competitions, results);
//     EXPECT_EQ(expected, actual) << "Test case " << i + 1 << " failed";
//   }
// }
