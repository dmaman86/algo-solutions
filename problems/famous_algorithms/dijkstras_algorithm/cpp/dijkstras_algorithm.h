#include <iostream>
#include <limits>
#include <queue>
#include <utility>
#include <vector>

typedef std::pair<int, int> pair;
typedef std::priority_queue<pair, std::vector<pair>, std::greater<pair>>
    minHeap;
typedef std::vector<std::vector<std::vector<int>>> graph;

void initDistance(int, int, std::vector<int> &);
void initQueue(int, minHeap &);
void relaxEdges(int, int, const graph &, std::vector<int> &, minHeap &);
void convertUnreachableToNegativeOne(std::vector<int> &);

std::vector<int> dijkstrasAlgorithm(int, graph);

// typedef std::pair<int, int> pair;
// typedef std::priority_queue<pair, std::vector<pair>, std::greater<pair>>
//     minHeap;
// typedef std::vector<std::vector<std::vector<int>>> graph;
//
// class DijkstrasAlgorithm {
// private:
//   void initDistance(std::vector<int> &, int, int);
//   void initQueue(int, minHeap &);
//   void relaxEdges(int, int, const graph &, std::vector<int> &, minHeap &);
//   void convertUnreachableToNegativeOne(std::vector<int> &);
//
// public:
//   DijkstrasAlgorithm() = default;
//   std::vector<int> calculate(int, const graph &);
// };
