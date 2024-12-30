#include "astar_algorithm.h"
#include <algorithm>
#include <cmath>
#include <queue>

int heuristic(Node a, Node b) {
  return std::abs(a.first - b.first) + std::abs(a.second - b.second);
}

std::vector<Node> getNeighbors(Node node, int rows, int cols) {
  std::vector<std::pair<int, int>> directions = {
      {1, 0}, {-1, 0}, {0, 1}, {0, -1}};
  std::vector<Node> neighbors;

  for (auto [dr, dc] : directions) {
    int newRow = node.first + dr;
    int newCol = node.second + dc;
    if (newRow >= 0 && newRow < rows && newCol >= 0 && newCol < cols) {
      neighbors.emplace_back(newRow, newCol);
    }
  }
  return neighbors;
}

std::vector<std::vector<int>>
reconstructPath(std::unordered_map<Node, Node, NodeHash> &cameFrom, Node start,
                Node end) {
  std::vector<std::vector<int>> path;
  Node current = end;

  while (cameFrom.find(current) != cameFrom.end()) {
    path.push_back({current.first, current.second});
    current = cameFrom[current];
  }
  path.push_back({start.first, start.second});
  std::reverse(path.begin(), path.end());
  return path;
}

std::vector<std::vector<int>>
aStarAlgorithm(int startRow, int startCol, int endRow, int endCol,
               std::vector<std::vector<int>> &graph) {
  int rows = graph.size();
  int cols = graph[0].size();

  Node start = {startRow, startCol};
  Node end = {endRow, endCol};

  std::priority_queue<std::pair<int, Node>, std::vector<std::pair<int, Node>>,
                      Compare>
      openSet;
  openSet.push({0, start});

  std::unordered_map<Node, Node, NodeHash> cameFrom;

  std::vector<std::vector<int>> gScore(rows, std::vector<int>(cols, INT_MAX));
  gScore[startRow][startCol] = 0;

  std::vector<std::vector<int>> fScore(rows, std::vector<int>(cols, INT_MAX));
  fScore[startRow][startCol] = heuristic(start, end);

  while (!openSet.empty()) {
    Node current = openSet.top().second;
    openSet.pop();

    if (current == end)
      return reconstructPath(cameFrom, start, end);

    for (Node neighbor : getNeighbors(current, rows, cols)) {
      int row = neighbor.first;
      int col = neighbor.second;

      if (graph[row][col] == 0) {
        int tentativeGScore = gScore[current.first][current.second] + 1;

        if (tentativeGScore < gScore[row][col]) {
          cameFrom[neighbor] = current;
          gScore[row][col] = tentativeGScore;
          fScore[row][col] = gScore[row][col] + heuristic(neighbor, end);

          openSet.push({fScore[row][col], neighbor});
        }
      }
    }
  }
  return {};
}
