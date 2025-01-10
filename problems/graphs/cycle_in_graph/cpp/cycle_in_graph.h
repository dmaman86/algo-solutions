#include <vector>

enum class VisitState { UNVISITED, VISITING, VISITED };

using vector2DInt = std::vector<std::vector<int>>;

void dfs(int, std::vector<VisitState> &, const vector2DInt &, bool &);
bool cycleInGraph(const vector2DInt &);
