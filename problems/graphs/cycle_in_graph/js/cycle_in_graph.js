export const cycleInGraph = (() => {
  const VisitState = { UNVISITED: 0, VISITING: 1, VISITED: 2 };

  const dfs = (node, visited, graph, state) => {
    if (state.haveCycle) return;
    if (visited[node] === VisitState.VISITING) {
      state.haveCycle = true;
      return;
    }

    visited[node] = VisitState.VISITING;
    for (const neighbor of graph[node]) {
      dfs(neighbor, visited, graph, state);
    }
    visited[node] = VisitState.VISITED;
  };

  return (graph) => {
    const visited = Array(graph.length).fill(VisitState.UNVISITED);
    const state = { haveCycle: false };

    for (let i = 0; i < graph.length && !state.haveCycle; i++) {
      dfs(i, visited, graph, state);
    }
    return state.haveCycle;
  };
})();
