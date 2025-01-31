#include "minimum_waiting_time.h"
#include <algorithm>

int minimumWaitingTime(std::vector<int> queries) {
  int total = 0, query = 0;
  std::sort(queries.begin(), queries.end());

  for (size_t i = 0; i < queries.size(); i++) {
    total += (query * (queries.size() - i));
    query = queries[i];
  }
  return total;
}
