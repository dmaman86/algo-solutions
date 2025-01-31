#include "count_squares.h"

#include <unordered_set>
#include <utility>

int countSquares(std::vector<std::vector<int>> points) {
  std::unordered_set<std::string> point_set;

  for (const auto &point : points) {
    point_set.insert(std::to_string(point[0]) + "," + std::to_string(point[1]));
  }
  int count = 0;
  std::vector<int> rotationClockwise = {0, 1, -1, 0};
  std::vector<int> rotationCounterClockwise = {0, -1, 1, 0};

  auto rotate = [](const std::pair<int, int> &point,
                   const std::vector<int> &matrix) -> std::pair<int, int> {
    int x = point.first, y = point.second;
    return {matrix[0] * x + matrix[1] * y, matrix[2] * x + matrix[3] * y};
  };

  auto checkSquare = [&](const std::pair<int, int> &p1,
                         const std::pair<int, int> &p2,
                         const std::pair<int, int> &vec,
                         const std::vector<int> &matrix) -> int {
    auto rotatedVec = rotate(vec, matrix);
    std::string p3 = std::to_string(p1.first + rotatedVec.first) + "," +
                     std::to_string(p1.second + rotatedVec.second);
    std::string p4 = std::to_string(p2.first + rotatedVec.first) + "," +
                     std::to_string(p2.second + rotatedVec.second);

    return (point_set.find(p3) != point_set.end() &&
            point_set.find(p4) != point_set.end())
               ? 1
               : 0;
  };

  for (int i = 0; i < points.size(); i++) {
    auto p1 = std::make_pair(points[i][0], points[i][1]);
    for (int j = i + 1; j < points.size(); j++) {
      auto p2 = std::make_pair(points[j][0], points[j][1]);

      int dx = p2.first - p1.first;
      int dy = p2.second - p1.second;

      count += checkSquare(p1, p2, {dx, dy}, rotationClockwise);
      count += checkSquare(p1, p2, {dx, dy}, rotationCounterClockwise);
    }
  }
  return count / 4;
}
