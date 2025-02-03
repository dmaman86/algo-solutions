#include "cycle_in_graph.h"
#include <functional>

bool cycleInGraph(const vector2DInt &edges) {
  std::vector<VisitState> visited(edges.size(), VisitState::UNVISITED);
  bool hasCycle = false;

  std::function<void(int)> dfs = [&](int node) -> void {
    if (hasCycle)
      return;

    if (visited[node] == VisitState::VISITING) {
      hasCycle = true;
      return;
    }
    visited[node] = VisitState::VISITING;
    for (int neighbor : edges[node]) {
      dfs(neighbor);
    }
    visited[node] = VisitState::VISITED;
  };

  for (size_t i = 0; i < edges.size() && !hasCycle; i++) {
    dfs(i);
  }
  return hasCycle;
}
