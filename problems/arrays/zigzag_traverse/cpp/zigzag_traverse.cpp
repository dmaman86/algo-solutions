#include "zigzag_traverse.h"
#include <algorithm>
#include <utility>

std::vector<int> zigzagTraverse(std::vector<std::vector<int>> array) {
  if (array.empty() || array[0].empty())
    return {};

  Dimension dimension = {(int)array.size(), (int)array[0].size()};
  Position position = {0, 0};
  std::vector<int> result;
  bool goingDown = true;

  std::pair<int, int> moveDown = {1, -1};
  std::pair<int, int> moveUp = {-1, 1};

  auto updatePosition = [&](int limit) {
    if (position.x == limit - 1)
      position.y++;
    else
      position.x++;
  };

  auto updateDirection = [&]() -> std::pair<bool, bool> {
    bool atBottomLeft =
        goingDown && (position.y == 0 || position.x == dimension.rows - 1);
    bool atTopRight =
        !goingDown && (position.x == 0 || position.y == dimension.cols - 1);

    if (atBottomLeft || atTopRight)
      goingDown = !goingDown;
    if (atTopRight)
      std::swap(position.x, position.y);

    return {atBottomLeft, atTopRight};
  };

  auto moveInZigzag = [&](const std::pair<int, int> &move) {
    auto [atBottomLeft, atTopRight] = updateDirection();

    if (atBottomLeft)
      updatePosition(dimension.rows);
    else if (atTopRight) {
      updatePosition(dimension.cols);
      std::swap(position.x, position.y);
    } else {
      position.x += move.first;
      position.y += move.second;
    }
  };

  while (result.size() < dimension.rows * dimension.cols) {
    result.push_back(array[position.x][position.y]);
    std::pair<int, int> move = goingDown ? moveDown : moveUp;
    moveInZigzag(move);
  }
  return result;
}
