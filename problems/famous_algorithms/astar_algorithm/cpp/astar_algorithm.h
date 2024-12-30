
#include <unordered_map>
#include <vector>

using Node = std::pair<int, int>;

struct NodeHash {
  std::size_t operator()(const Node &node) const {
    return std::hash<int>()(node.first) ^ (std::hash<int>()(node.second) << 1);
  }
};

struct Compare {
  bool operator()(std::pair<int, Node> a, std::pair<int, Node> b) {
    return a.first > b.first;
  }
};

int heuristic(Node, Node);

std::vector<Node> getNeighbors(Node, int, int);

std::vector<std::vector<int>>
reconstructPath(std::unordered_map<Node, Node, NodeHash> &, Node, Node);

std::vector<std::vector<int>> aStarAlgorithm(int, int, int, int,
                                             std::vector<std::vector<int>> &);
