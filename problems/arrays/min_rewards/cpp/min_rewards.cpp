#include "min_rewards.h"
#include <algorithm>
#include <numeric>

int minRewards(std::vector<int> scores) {
  int n = scores.size();
  std::vector<int> rewards(n, 1);

  auto traverse = [&](int startIdx, int endIdx, int step) {
    for (int i = startIdx; i != endIdx; i += step) {
      if (scores[i] > scores[i - step]) {
        rewards[i] = (step == 1) ? rewards[i - step] + 1
                                 : std::max(rewards[i], rewards[i - step] + 1);
      }
    }
  };

  traverse(1, n, 1);
  traverse(n - 2, -1, -1);

  return std::accumulate(rewards.begin(), rewards.end(), 0);
}
