#include <functional>
#include <vector>

typedef std::function<int(int)> moveOperation;

class FourNumberSumSolver {
public:
  std::vector<std::vector<int>> fourNumberSum(std::vector<int>, int);
};
