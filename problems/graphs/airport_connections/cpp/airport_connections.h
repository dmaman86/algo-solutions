#include <stack>
#include <unordered_map>
#include <unordered_set>
#include <vector>

using Airports = std::vector<std::string>;
using Routes = std::vector<Airports>;
using AirportGraph = std::unordered_map<std::string, Airports>;

void dfs(const AirportGraph &, const std::string &,
         std::unordered_set<std::string> &,
         std::stack<std::string> * = nullptr);

AirportGraph buildGraph(const Airports &, const Routes &);

int airportConnections(const Airports &, const Routes &, const std::string &);
