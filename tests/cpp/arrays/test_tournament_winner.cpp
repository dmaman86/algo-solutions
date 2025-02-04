#include "../../../problems/arrays/tournament_winner/cpp/tournament_winner.h"
#include "../jsontestbase.h"

#include <vector>

class TournamentWinnerTest : public JsonTestBase {
public:
  TournamentWinnerTest() {
    json_file_path =
        std::string(TEST_CASES_DIR) + "/arrays/tournament_winner.json";
  }
};

TEST_F(TournamentWinnerTest, TestCases) {
  ASSERT_FALSE(test_cases.empty()) << "Test cases are empty";
  for (auto &test : test_cases) {
    std::vector<std::vector<std::string>> competitions = test["competitions"];
    std::vector<int> results = test["results"];
    std::string expected = test["expected"];
    std::string actual = tournamentWinner(competitions, results);
    EXPECT_EQ(expected, actual) << "Failed on test case: " << test.dump(2);
  }
}
