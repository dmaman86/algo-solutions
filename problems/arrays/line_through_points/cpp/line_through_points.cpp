#include "line_through_points.h"
#include <algorithm>
#include <map>

std::pair<int, int> normalizeSlope(int dx, int dy,
                                   const std::function<int(int, int)> &gcd) {
  int gcdVal = gcd(dx, dy);
  dx /= gcdVal;
  dy /= gcdVal;

  if (dx < 0 || (dy == 0 && dx < 0)) {
    dx = -dx;
    dy = -dy;
  }
  return std::make_pair(dx, dy);
}

int getMaxPoints(size_t index, const std::vector<std::vector<int>> &points,
                 const std::function<int(int, int)> &gcd,
                 const std::pair<int, int> &p1) {
  std::map<std::string, int> slopes;
  int duplicate = 1;
  int localMax = 0;

  for (size_t j = index + 1; j < points.size(); j++) {
    std::pair<int, int> p2 = std::make_pair(points[j][0], points[j][1]);
    if (p1 == p2) {
      duplicate++;
      continue;
    }
    std::pair<int, int> normalize =
        normalizeSlope(p2.first - p1.first, p2.second - p1.second, gcd);
    std::string slope = std::to_string(normalize.second) + "/" +
                        std::to_string(normalize.first);
    slopes[slope]++;
    localMax = std::max(localMax, slopes[slope]);
  }
  return localMax + duplicate;
}

int lineThroughPoints(std::vector<std::vector<int>> points) {
  if (points.size() < 3)
    return points.size();

  std::function<int(int, int)> gcd = [&](int a, int b) {
    return b == 0 ? a : gcd(b, a % b);
  };

  int max_points = 0;
  for (size_t i = 0; i < points.size(); i++) {
    max_points = std::max(
        max_points, getMaxPoints(i, points, gcd,
                                 std::make_pair(points[i][0], points[i][1])));
  }
  return max_points;
}
