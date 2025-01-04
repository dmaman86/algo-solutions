#include "subarray_sort.h"
#include <algorithm>

int findBoundary(const std::vector<int> &array, int init,
                 std::function<bool(int, const std::vector<int> &)> condition,
                 int step) {
  int index = init;
  while (condition(index, array))
    index += step;

  return index;
}

std::vector<int> subarraySort(std::vector<int> array) {
  if (array.size() == 1)
    return {-1, -1};

  int left = findBoundary(
      array, 0,
      [](int index, const std::vector<int> &arr) {
        return index < arr.size() - 1 && arr[index] <= arr[index + 1];
      },
      1);

  if (left == array.size() - 1)
    return {-1, -1};

  int right = findBoundary(
      array, array.size() - 1,
      [](int index, const std::vector<int> &arr) {
        return index > 0 && arr[index] >= arr[index - 1];
      },
      -1);

  int min_val =
      *std::min_element(array.begin() + left, array.begin() + right + 1);
  int max_val =
      *std::max_element(array.begin() + left, array.begin() + right + 1);

  left = findBoundary(
      array, left,
      [min_val](int index, const std::vector<int> &arr) {
        return index > 0 && arr[index - 1] > min_val;
      },
      -1);

  right = findBoundary(
      array, right,
      [max_val](int index, const std::vector<int> &arr) {
        return index < arr.size() - 1 && arr[index + 1] < max_val;
      },
      1);

  return {left, right};
}
