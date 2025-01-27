#include "longest_increasing_subsequence.h"
#include <algorithm>

std::pair<int, std::vector<int>> buildListData(const std::vector<int> &array) {
  std::vector<int> lisValues, indices, predecessor(array.size(), -1);

  for (size_t i = 0; i < array.size(); i++) {
    auto it = std::lower_bound(lisValues.begin(), lisValues.end(), array[i]);

    if (it == lisValues.end()) {
      if (!indices.empty())
        predecessor[i] = indices.back();
      indices.push_back(i);
      lisValues.push_back(array[i]);
    } else {
      auto pos = it - lisValues.begin();
      if (pos > 0)
        predecessor[i] = indices[pos - 1];
      indices[pos] = i;
      lisValues[pos] = array[i];
    }
  }
  return {indices.back(), predecessor};
}

std::vector<int> longestIncreasingSubsequence(std::vector<int> array) {
  if (array.empty())
    return {};

  auto [lastIndex, predecessor] = buildListData(array);
  std::vector<int> result;

  while (lastIndex != -1) {
    result.push_back(array[lastIndex]);
    lastIndex = predecessor[lastIndex];
  }
  std::reverse(result.begin(), result.end());
  return result;
}
