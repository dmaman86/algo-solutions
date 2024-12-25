export const fourNumberSum = (array, targetSum) => {
  array.sort((a, b) => a - b);
  const result = [];

  const skipDuplicates = (arr, index, bound, step) => {
    while (index !== bound && arr[index] === arr[index + step]) {
      index += step;
    }
    if (index !== bound) index += step;
    return index;
  };

  const isDuplicate = (arr, index, bound, prevIndex) => {
    return index > bound && arr[index] === arr[prevIndex];
  };

  for (let i = 0; i < array.length; i++) {
    if (isDuplicate(array, i, 0, i - 1)) continue;

    for (let j = i + 1; j < array.length; j++) {
      if (isDuplicate(array, j, i + 1, j - 1)) continue;

      let left = j + 1;
      let right = array.length - 1;

      while (left < right) {
        const sum = array[i] + array[j] + array[left] + array[right];

        if (sum < targetSum) left++;
        else if (sum > targetSum) right--;
        else {
          result.push([array[i], array[j], array[left], array[right]]);
          left = skipDuplicates(array, left, right, 1);
          right = skipDuplicates(array, right, left, -1);
        }
      }
    }
  }
  return result;
};
