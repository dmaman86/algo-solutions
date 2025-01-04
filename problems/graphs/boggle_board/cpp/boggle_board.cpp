#include "boggle_board.h"
#include <functional>
#include <unordered_set>

List boggleBoard(Board &board, List &words) {
  List foundWords;
  std::unordered_set<std::string> remainingWords(words.begin(), words.end());
  Trie trie;

  for (const auto &word : words) {
    trie.insert(word);
  }

  auto rows = board.size();
  auto cols = board[0].size();

  std::vector<std::vector<bool>> visited(rows, std::vector<bool>(cols, false));

  std::vector<std::pair<int, int>> directions = {
      {-1, -1}, {-1, 0}, {-1, 1}, {0, -1}, {0, 1}, {1, -1}, {1, 0}, {1, 1}};

  std::function<void(int, int, TrieNode *, std::string &)> dfs =
      [&](int x, int y, TrieNode *node, std::string &path) {
        if (x < 0 || y < 0 || x >= rows || y >= cols || visited[x][y])
          return;

        TrieNode *childNode = node->getChild(board[x][y]);
        if (!childNode)
          return;

        visited[x][y] = true;
        path.push_back(board[x][y]);

        if (childNode->isEndOfWord) {
          foundWords.push_back(path);
          remainingWords.erase(path);
          childNode->isEndOfWord = false;
        }

        for (const auto &[dx, dy] : directions) {
          dfs(x + dx, y + dy, childNode, path);
        }

        visited[x][y] = false;
        path.pop_back();
      };

  for (int i = 0; i < rows; i++) {
    for (int j = 0; j < cols; j++) {
      if (remainingWords.empty())
        break;
      std::string currentPath;
      dfs(i, j, trie.getRoot(), currentPath);
    }
    if (remainingWords.empty())
      break;
  }
  return foundWords;
}
