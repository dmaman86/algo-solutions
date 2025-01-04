#include <functional>
#include <vector>

int findBoundary(const std::vector<int> &, int,
                 std::function<bool(int, const std::vector<int> &)>, int);
std::vector<int> subarraySort(std::vector<int>);
