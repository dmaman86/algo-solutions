#include <utility>
#include <vector>

using vector2DInt = std::vector<std::vector<int>>;
using Dimensions = std::pair<int, int>;

vector2DInt buildDp(const vector2DInt &);
int findMaxSum(const vector2DInt &, int, const Dimensions &);
int maximumSumSubmatrix(vector2DInt, int);
