#include "same_bsts.h"
#include <utility>

bool sameBsts(const std::vector<int> &arrayOne,
              const std::vector<int> &arrayTwo) {

  if (arrayOne.empty() && arrayTwo.empty())
    return true;

  if ((arrayOne.size() != arrayTwo.size()) || (arrayOne[0] != arrayTwo[0]))
    return false;

  auto getChildren = [](const std::vector<int> &array)
      -> std::pair<std::vector<int>, std::vector<int>> {
    std::vector<int> smaller, greaterOrEqual;

    for (size_t i = 1; i < array.size(); i++) {
      if (array[i] < array[0])
        smaller.push_back(array[i]);
      else
        greaterOrEqual.push_back(array[i]);
    }

    return {smaller, greaterOrEqual};
  };

  auto [leftOne, rightOne] = getChildren(arrayOne);
  auto [leftTwo, rightTwo] = getChildren(arrayTwo);

  return sameBsts(leftOne, leftTwo) && sameBsts(rightOne, rightTwo);
}
