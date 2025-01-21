export const taskAssignment = (k, tasks) => {
  // pair each task value with its original index
  const taskPairs = tasks.map((task, index) => [task, index]);

  // sort the tasks by their values
  taskPairs.sort((a, b) => a[0] - b[0]);

  // pair the smallest and largest tasks
  const result = [];
  for (let i = 0; i < k; i++) {
    result.push([taskPairs[i][1], taskPairs[taskPairs.length - 1 - i][1]]);
  }

  return result;
};
