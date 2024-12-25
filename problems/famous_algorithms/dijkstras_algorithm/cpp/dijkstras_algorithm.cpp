#include "dijkstras_algorithm.h"

void initDistance(int n, int start, std::vector<int> &distances) {
  distances.resize(n, std::numeric_limits<int>::max());
  distances[start] = 0;
}

void initQueue(int start, minHeap &pq) { pq.push({0, start}); }

void relaxEdges(int currentVertex, int currentDistance, const graph &edges,
                std::vector<int> &distances, minHeap &pq) {
  for (const auto &edge : edges[currentVertex]) {
    if (edge.size() != 2)
      continue;
    int neighbor = edge[0];
    int weight = edge[1];
    int newDistance = currentDistance + weight;

    if (newDistance < distances[neighbor]) {
      distances[neighbor] = newDistance;
      pq.push({newDistance, neighbor});
    }
  }
}

void convertUnreachableToNegativeOne(std::vector<int> &distances) {
  for (int &distance : distances) {
    if (distance == std::numeric_limits<int>::max()) {
      distance = -1;
    }
  }
}

// std::vector<int> dijkstrasAlgorithm(int start, graph edges) {
//   int V = edges.size();
//   std::vector<int> distance(V, std::numeric_limits<int>::max());
//
//   distance[start] = 0;
//   std::vector<bool> visited(V, false);
//   std::vector<bool> distance_found(V, false);
//   distance_found[start] = true;
//
//   minHeap pq;
//   pq.push({0, start});
//
//   while (!pq.empty()) {
//     int u = pq.top().second;
//     pq.pop();
//     visited[u] = true;
//
//     for (auto neighbor : edges[u]) {
//       int v = neighbor[0];
//       int weight = neighbor[1];
//       if (!visited[v] && distance[u] + weight < distance[v]) {
//         distance[v] = distance[u] + weight;
//         pq.push({distance[v], v});
//         distance_found[v] = true;
//       }
//     }
//   }
//   for (int i = 0; i < V; i++) {
//     if (!distance_found[i])
//       distance[i] = -1;
//   }
//   return distance;
// }

std::vector<int> dijkstrasAlgorithm(int start, graph edges) {
  minHeap pq;
  std::vector<int> distances;

  initDistance(edges.size(), start, distances);
  initQueue(start, pq);

  while (!pq.empty()) {
    auto [currentDistance, currentVertex] = pq.top();
    pq.pop();

    if (currentDistance > distances[currentVertex]) {
      continue;
    }
    relaxEdges(currentVertex, currentDistance, edges, distances, pq);
  }
  convertUnreachableToNegativeOne(distances);
  return distances;
}
