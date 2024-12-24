export const topologicalSort = (() => {
  const State = {
    UNVISITED: 0,
    VISITING: 1,
    VISITED: 2,
  };

  const dfs = (job, graph, states, order) => {
    states.set(job, State.VISITING);

    const dependencies = graph.get(job) || [];
    for (const dep of dependencies) {
      if (states.get(dep) === State.VISITING) return false;
      else if (states.get(dep) === State.UNVISITED) {
        if (!dfs(dep, graph, states, order)) return false;
      }
    }

    states.set(job, State.VISITED);
    order.push(job);
    return true;
  };

  const initGraphStates = (graph, states, jobs) => {
    for (const job of jobs) {
      graph.set(job, []);
      states.set(job, State.UNVISITED);
    }
  };

  const buildGraph = (graph, deps) => {
    for (const [prereq, job] of deps) {
      if (!graph.has(prereq)) graph.set(prereq, []);
      graph.get(prereq).push(job);
    }
  };

  const topologicalSort = (jobs, deps) => {
    if (!Array.isArray(jobs) || !Array.isArray(deps)) {
      throw new Error("Invalid input: jobs and deps should be an array");
    }

    const graph = new Map();
    const states = new Map();
    const order = [];

    initGraphStates(graph, states, jobs);
    buildGraph(graph, deps);

    for (const job of jobs) {
      if (states.get(job) === State.UNVISITED) {
        if (!dfs(job, graph, states, order)) return []; // cycle detected
      }
    }
    return order.reverse();
  };

  return { topologicalSort };
})();
