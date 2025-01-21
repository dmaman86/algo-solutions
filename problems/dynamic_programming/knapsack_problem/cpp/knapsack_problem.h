#include <vector>

using vectorInt = std::vector<int>;
using vector2DInt = std::vector<vectorInt>;

vector2DInt fillDpMatrix(const vector2DInt &, int);
vectorInt getSelectedItems(const vector2DInt &, const vector2DInt &, int);
vector2DInt knapsackProblem(vector2DInt, int);
