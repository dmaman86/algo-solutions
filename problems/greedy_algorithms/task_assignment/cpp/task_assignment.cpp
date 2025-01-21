#include "task_assignment.h"

#include <algorithm>

vvi taskAssignment(int k, std::vector<int> tasks) {
  // result container for pairs of tasks indices
  vvi result;

  // pair task values with their original indices
  vpi taskPairs;
  for (int i = 0; i < tasks.size(); i++) {
    taskPairs.push_back({tasks[i], i});
  }

  // sort tasks by their values
  std::sort(taskPairs.begin(), taskPairs.end());

  // pair smallest and largest tasks
  for (int i = 0; i < k; i++) {
    result.push_back(
        {taskPairs[i].second, taskPairs[taskPairs.size() - i - 1].second});
  }
  return result;
}
