#include <vector>

struct Point {
  int x, y;

  Point &operator+=(const Point &other) {
    x += other.x;
    y += other.y;
    return *this;
  }

  bool operator<(const Point &other) const {
    return x < other.x && y < other.y;
  }
};

std::vector<int> zigzagTraverse(std::vector<std::vector<int>>);
