#include "topological_sort.h"

bool dfs(int job, std::unordered_map<int, std::vector<int>> &graph,
         std::unordered_map<int, State> &states, std::stack<int> &order) {
  states[job] = VISITING;

  for (int dep : graph[job]) {
    if (states[dep] == VISITING)
      return false;
    else if (states[dep] == UNVISITED) {
      if (!dfs(dep, graph, states, order))
        return false;
    }
  }
  states[job] = VISITED;
  order.push(job);
  return true;
}

void initGraphStates(std::unordered_map<int, std::vector<int>> &graph,
                     std::unordered_map<int, State> &states,
                     const std::vector<int> &jobs) {
  for (int job : jobs) {
    graph[job] = std::vector<int>();
    states[job] = UNVISITED;
  }
}

void buildGraph(std::unordered_map<int, std::vector<int>> &graph,
                const std::vector<std::vector<int>> &deps) {

  for (const auto &dep : deps) {
    int prereq = dep[0];
    int job = dep[1];
    graph[prereq].push_back(job);
  }
}

std::vector<int> topologicalSort(std::vector<int> jobs,
                                 std::vector<std::vector<int>> deps) {
  std::unordered_map<int, std::vector<int>> graph;
  std::unordered_map<int, State> states;

  initGraphStates(graph, states, jobs);

  buildGraph(graph, deps);

  std::stack<int> order;
  for (int job : jobs) {
    if (states[job] == UNVISITED) {
      if (!dfs(job, graph, states, order))
        return {};
    }
  }
  std::vector<int> sortedJobs;
  while (!order.empty()) {
    sortedJobs.push_back(order.top());
    order.pop();
  }
  return sortedJobs;
}
