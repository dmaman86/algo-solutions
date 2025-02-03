#include <vector>

enum class VisitState { UNVISITED, VISITING, VISITED };

using vector2DInt = std::vector<std::vector<int>>;

bool cycleInGraph(const vector2DInt &);
