export const airportConnections = (() => {
  const dfs = (graph, airport, visited, stack = null) => {
    visited.add(airport);

    for (const neighbor of graph[airport]) {
      if (!visited.has(neighbor)) {
        dfs(graph, neighbor, visited, stack);
      }
    }
    if (stack) stack.push(airport);
  };

  const airportConnections = (airports, routes, startingAirport) => {
    const graph = {};
    for (const airport of airports) {
      graph[airport] = [];
    }

    for (const [from, to] of routes) {
      if (graph[from]) graph[from].push(to);
    }

    const visited = new Set();
    const stack = [];
    for (const airport of airports) {
      if (!visited.has(airport)) {
        dfs(graph, airport, visited, stack);
      }
    }
    const reachable = new Set();
    dfs(graph, startingAirport, reachable);

    let newConnections = 0;
    while (stack.length) {
      const airport = stack.pop();

      if (!reachable.has(airport)) {
        newConnections++;
        dfs(graph, airport, reachable);
      }
    }
    return newConnections;
  };

  return airportConnections;
})();
