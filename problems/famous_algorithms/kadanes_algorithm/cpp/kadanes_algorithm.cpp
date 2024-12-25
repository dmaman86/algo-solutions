#include "kadanes_algorithm.h"

int kadanesAlgorithm(std::vector<int> array) {
  int max_so_far = INT_MIN, max_ending_here = 0;

  for (auto it = array.begin(); it != array.end(); it++) {
    max_ending_here += *it;
    max_so_far = std::max(max_ending_here, max_so_far);

    if (max_ending_here < 0)
      max_ending_here = 0;
  }

  return max_so_far;
}
