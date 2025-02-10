#include "zigzag_traverse.h"
#include <utility>

std::vector<int> zigzagTraverse(std::vector<std::vector<int>> array) {
  if (array.empty() || array[0].empty())
    return {};

  Point point = {0, 0};
  Point dimension = {(int)array.size(), (int)array[0].size()};
  std::vector<int> result;
  bool goingDown = true;

  Point moveDown = {1, -1};
  Point moveUp = {-1, 1};

  auto checkBoundary = [&]() -> std::pair<bool, bool> {
    bool atBottomLeft =
        goingDown && (point.y == 0 || point.x == dimension.x - 1);
    bool atTopRight =
        !goingDown && (point.x == 0 || point.y == dimension.y - 1);

    if (atBottomLeft || atTopRight)
      goingDown = !goingDown;

    return {atBottomLeft, atTopRight};
  };

  auto nextPosition = [&](const bool &atTopRight) {
    Point position = atTopRight ? Point{point.y, point.x} : point;
    int limit = atTopRight ? dimension.y : dimension.x;

    if (position.x == limit - 1)
      position.y++;
    else
      position.x++;

    return atTopRight ? Point{position.y, position.x} : position;
  };

  while (result.size() < dimension.x * dimension.y) {
    if (point < dimension)
      result.push_back(array[point.x][point.y]);

    auto [atBottomLeft, atTopRight] = checkBoundary();
    if (!atBottomLeft && !atTopRight)
      point += goingDown ? moveDown : moveUp;
    else
      point = nextPosition(atTopRight);
  }
  return result;
}
