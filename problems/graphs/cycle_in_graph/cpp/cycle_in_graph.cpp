#include "cycle_in_graph.h"

void dfs(int node, std::vector<VisitState> &visited, const vector2DInt &edges,
         bool &hasCycle) {
  if (hasCycle)
    return;
  if (visited[node] == VisitState::VISITING) {
    hasCycle = true;
    return;
  }
  visited[node] = VisitState::VISITING;
  for (int neighbor : edges[node]) {
    dfs(neighbor, visited, edges, hasCycle);
  }
  visited[node] = VisitState::VISITED;
}

bool cycleInGraph(const vector2DInt &edges) {
  std::vector<VisitState> visited(edges.size(), VisitState::UNVISITED);
  bool hasCycle = false;

  for (size_t i = 0; i < edges.size() && !hasCycle; i++) {
    dfs(i, visited, edges, hasCycle);
  }
  return hasCycle;
}
