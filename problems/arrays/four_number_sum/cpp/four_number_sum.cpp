#include "four_number_sum.h"
#include <algorithm>

std::vector<std::vector<int>>
FourNumberSumSolver::fourNumberSum(std::vector<int> array, int targetSum) {
  std::sort(array.begin(), array.end());
  std::vector<std::vector<int>> result;

  auto skipDuplicates = [](const std::vector<int> &array, size_t &index,
                           size_t bound, int step) {
    while (index != bound && array[index] == array[index + step]) {
      index += step;
    }
    if (index != bound)
      index += step;
  };

  auto isDuplicate = [](const std::vector<int> &array, size_t index,
                        size_t bound, size_t prevIndex) {
    return index > bound && array[index] == array[prevIndex];
  };

  for (size_t i = 0; i < array.size(); i++) {
    if (isDuplicate(array, i, 0, i - 1))
      continue;

    for (size_t j = i + 1; j < array.size(); j++) {
      if (isDuplicate(array, j, i + 1, j - 1))
        continue;

      auto left = j + 1;
      auto right = array.size() - 1;

      while (left < right) {
        auto sum = array[i] + array[j] + array[left] + array[right];

        if (sum < targetSum) {
          left++;
        } else if (sum > targetSum) {
          right--;
        } else {
          result.push_back({array[i], array[j], array[left], array[right]});
          skipDuplicates(array, left, right, 1);
          skipDuplicates(array, right, left, -1);
        }
      }
    }
  }
  return result;
}
