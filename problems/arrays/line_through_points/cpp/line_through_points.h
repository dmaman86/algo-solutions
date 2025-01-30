#include <functional>
#include <utility>
#include <vector>

std::pair<int, int> normalizeSlope(int, int,
                                   const std::function<int(int, int)> &);
int getMaxPoints(size_t, const std::vector<std::vector<int>> &,
                 const std::function<int(int, int)> &,
                 const std::pair<int, int> &);
int lineThroughPoints(std::vector<std::vector<int>>);
