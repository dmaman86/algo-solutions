#include "airport_connections.h"

void dfs(const AirportGraph &graph, const std::string &airport,
         std::unordered_set<std::string> &visited,
         std::stack<std::string> *order) {

  visited.insert(airport);

  if (graph.find(airport) != graph.end()) {
    for (const auto &neighbor : graph.at(airport)) {
      if (visited.find(neighbor) == visited.end()) {
        dfs(graph, neighbor, visited, order);
      }
    }
  }

  if (order)
    order->push(airport);
}

int airportConnections(const Airports &airports, const Routes &routes,
                       const std::string &startingAirport) {

  AirportGraph graph;
  for (const auto &airport : airports) {
    graph[airport] = {};
  }
  for (const auto &route : routes) {
    if (graph.find(route[0]) != graph.end())
      graph[route[0]].push_back(route[1]);
  }

  std::unordered_set<std::string> visited;
  std::stack<std::string> order;
  for (const auto &airport : airports) {
    if (visited.find(airport) == visited.end()) {
      dfs(graph, airport, visited, &order);
    }
  }

  visited.clear();
  dfs(graph, startingAirport, visited);

  int new_connections = 0;
  while (!order.empty()) {
    std::string airport = order.top();
    order.pop();

    if (visited.find(airport) == visited.end()) {
      new_connections++;
      dfs(graph, airport, visited);
    }
  }
  return new_connections;
}
