#include "kruskals_algorithm.h"
#include <algorithm>
#include <numeric>
#include <tuple>

int find(vector<int> &parent, int x) {
  if (parent[x] != x) {
    parent[x] = find(parent, parent[x]);
  }
  return parent[x];
}

bool unionSets(vector<int> &parent, vector<int> &rank, int x, int y) {
  int rootX = find(parent, x);
  int rootY = find(parent, y);

  if (rootX != rootY) {
    if (rank[rootX] > rank[rootY]) {
      parent[rootY] = rootX;
    } else if (rank[rootX] < rank[rootY]) {
      parent[rootX] = rootY;
    } else {
      parent[rootY] = rootX;
      rank[rootX]++;
    }
    return true;
  }
  return false;
}

vector<vector<vector<int>>>
kruskalsAlgorithm(const vector<vector<vector<int>>> &edges) {
  int n = edges.size();
  vector<tuple<int, int, int>> allEdges;

  for (int u = 0; u < n; u++) {
    for (const auto &edge : edges[u]) {
      int v = edge[0];
      int w = edge[1];
      if (u < v)
        allEdges.emplace_back(w, u, v);
    }
  }

  sort(allEdges.begin(), allEdges.end());

  vector<int> parent(n);
  vector<int> rank(n, 0);
  iota(parent.begin(), parent.end(), 0);

  vector<vector<vector<int>>> mst(n);

  for (const auto &[w, u, v] : allEdges) {
    if (unionSets(parent, rank, u, v)) {
      mst[u].push_back({v, w});
      mst[v].push_back({u, w});
    }
  }

  for (int i = 0; i < n; i++) {
    sort(mst[i].begin(), mst[i].end());
  }
  return mst;
}
