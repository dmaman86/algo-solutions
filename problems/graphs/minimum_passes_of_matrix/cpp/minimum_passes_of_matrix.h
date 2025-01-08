#include <queue>
#include <vector>

using vvi = std::vector<std::vector<int>>;
using pair = std::pair<int, int>;

const std::vector<pair> movements = {{0, -1}, {0, 1}, {-1, 0}, {1, 0}};

bool isValid(const pair &, const vvi &);
std::queue<pair> initQueue(const vvi &, int &);
int bfs(vvi &, std::queue<pair> &, int &);
int minimumPassesOfMatrix(vvi matrix);
