#include "prims_algorithm.h"
#include <tuple>
#include <unordered_set>

using Edge = std::tuple<int, int, int>;
using PriorityQueue =
    std::priority_queue<Edge, std::vector<Edge>, std::greater<Edge>>;
using HashSet = std::unordered_set<int>;

AdjacencyList primsAlgorithm(const AdjacencyList &edges) {
  AdjacencyList mstEdges(edges.size());

  PriorityQueue minHeap;

  HashSet visited;

  for (auto edge : edges[0]) {
    minHeap.push(std::make_tuple(edge.back(), 0, edge.front()));
  }

  visited.insert(0);

  while (!minHeap.empty()) {
    auto [w, v1, v2] = minHeap.top();
    minHeap.pop();

    if (visited.count(v2)) {
      continue;
    }

    visited.insert(v2);
    mstEdges[v1].push_back({v2, w});
    mstEdges[v2].push_back({v1, w});

    for (auto edge : edges[v2]) {
      if (!visited.count(edge.front())) {
        minHeap.push(std::make_tuple(edge.back(), v2, edge.front()));
      }
    }

    for (int i = 0; i < edges.size(); i++) {
      sort(mstEdges[i].begin(), mstEdges[i].end());
    }
  }

  return mstEdges;
}
