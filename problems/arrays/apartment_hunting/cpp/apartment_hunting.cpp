#include "apartment_hunting.h"

#include <algorithm>

int apartmentHunting(std::vector<std::unordered_map<std::string, bool>> blocks,
                     std::vector<std::string> reqs) {
  int n = blocks.size();

  auto getMinDistances = [&]() {
    std::unordered_map<std::string, std::vector<int>> minDistances;
    for (const auto &req : reqs)
      minDistances[req] = std::vector<int>(n, std::numeric_limits<int>::max());

    auto calculateDistances = [&](int startIdx, int endIdx, int step) {
      for (const auto &req : reqs) {
        int closest = -1;
        for (int i = startIdx; i != endIdx; i += step) {
          if (blocks[i].count(req) && blocks[i].at(req))
            closest = i;
          if (closest != -1)
            minDistances[req][i] =
                std::min(minDistances[req][i], abs(i - closest));
        }
      }
    };
    calculateDistances(0, n, 1);
    calculateDistances(n - 1, -1, -1);

    return minDistances;
  };

  std::unordered_map<std::string, std::vector<int>> minDistances =
      getMinDistances();

  std::vector<int> maxDistancesAtBlocks(n, 0);
  for (int i = 0; i < n; i++) {
    int maxDistance = -1;
    for (const auto &req : reqs)
      maxDistance = std::max(maxDistance, minDistances[req][i]);

    maxDistancesAtBlocks[i] = maxDistance;
  }

  return std::min_element(maxDistancesAtBlocks.begin(),
                          maxDistancesAtBlocks.end()) -
         maxDistancesAtBlocks.begin();
}
