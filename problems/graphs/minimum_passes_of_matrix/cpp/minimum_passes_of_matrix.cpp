#include "minimum_passes_of_matrix.h"
#include <algorithm>

bool isValid(const pair &point, const vvi &matrix) {
  return (point.first >= 0 && point.first < matrix.size() &&
          point.second >= 0 && point.second < matrix[0].size());
}

std::queue<pair> initQueue(const vvi &matrix, int &negatives) {
  std::queue<pair> q;
  negatives = 0;

  for (size_t i = 0; i < matrix.size(); i++) {
    for (size_t j = 0; j < matrix[0].size(); j++) {
      if (matrix[i][j] > 0)
        q.push({i, j});
      else if (matrix[i][j] < 0)
        negatives++;
    }
  }
  return q;
}

int bfs(vvi &matrix, std::queue<pair> &q, int &negatives) {
  int passes = 0;

  while (!q.empty()) {
    auto size = q.size();
    bool converted = false;

    for (size_t i = 0; i < size; i++) {
      auto [x, y] = q.front();
      q.pop();

      for (const auto &[dx, dy] : movements) {
        int r = x + dx, c = y + dy;

        if (isValid({r, c}, matrix) && matrix[r][c] < 0) {
          matrix[r][c] = std::abs(matrix[r][c]);
          q.push({r, c});
          negatives--;
          converted = true;
        }
      }
    }
    if (converted)
      passes++;
  }
  return passes;
}

int minimumPassesOfMatrix(vvi matrix) {
  if (matrix.empty() || matrix[0].empty())
    return -1;

  int negatives = 0;
  std::queue<pair> q = initQueue(matrix, negatives);

  if (negatives == 0)
    return 0;

  int passes = bfs(matrix, q, negatives);

  return negatives == 0 ? passes : -1;
}
