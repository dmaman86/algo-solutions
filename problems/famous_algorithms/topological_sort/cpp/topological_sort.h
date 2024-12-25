#include <stack>
#include <unordered_map>
#include <unordered_set>
#include <vector>

enum State { UNVISITED, VISITING, VISITED };

bool dfs(int, std::unordered_map<int, std::vector<int>> &,
         std::unordered_map<int, State> &, std::stack<int> &);
void initGraphStates(std::unordered_map<int, std::vector<int>> &,
                     std::unordered_map<int, State> &,
                     const std::vector<int> &);
void buildGraph(std::unordered_map<int, std::vector<int>> &,
                const std::vector<std::vector<int>> &);
std::vector<int> topologicalSort(std::vector<int>,
                                 std::vector<std::vector<int>>);
