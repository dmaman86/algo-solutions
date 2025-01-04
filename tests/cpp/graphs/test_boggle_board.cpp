#include "../../../problems/graphs/boggle_board/cpp/boggle_board.h"
#include "../jsontestbase.h"
#include <gtest/gtest.h>
#include <nlohmann/json.hpp>
#include <string>
#include <unordered_set>
#include <vector>

using Board = std::vector<std::vector<char>>;
using List = std::vector<std::string>;

class BoggleBoardTest : public JsonTestBase {
public:
  BoggleBoardTest() {
    json_file_path = std::string(TEST_CASES_DIR) + "/graphs/boggle_board.json";
  }
};

Board convertToBoard(const std::vector<std::vector<std::string>> &raw_board) {
  Board board;
  for (const auto &row : raw_board) {
    std::vector<char> board_row;
    for (const auto &cell : row) {
      board_row.push_back(cell[0]);
    }
    board.push_back(board_row);
  }
  return board;
}

TEST_F(BoggleBoardTest, TestCases) {
  ASSERT_FALSE(test_cases.empty()) << "Test cases are empty";

  for (const auto &test : test_cases) {
    auto raw_board = test["board"].get<std::vector<std::vector<std::string>>>();
    auto board = convertToBoard(raw_board);
    auto words = test["words"].get<List>();
    auto expected = test["expected"].get<List>();

    auto result = boggleBoard(board, words);

    std::unordered_set<std::string> result_set(result.begin(), result.end());
    std::unordered_set<std::string> expected_set(expected.begin(),
                                                 expected.end());

    EXPECT_EQ(result_set, expected_set)
        << "Failed test case at index: " << test.dump(2);
  }
}
