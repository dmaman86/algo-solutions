export const subarraySort = (() => {
  const findBoundary = (array, init, condition, step) => {
    let index = init;
    while (condition(index, array)) {
      index += step;
    }
    return index;
  };

  return (array) => {
    if (array.length <= 1) return [-1, -1];

    let left = findBoundary(
      array,
      0,
      (index, arr) => index < arr.length - 1 && arr[index] <= arr[index + 1],
      1,
    );

    if (left === array.length - 1) return [-1, -1];

    let right = findBoundary(
      array,
      array.length - 1,
      (index, arr) => index > 0 && arr[index] >= arr[index - 1],
      -1,
    );

    const subarray = array.slice(left, right + 1);
    const min = Math.min(...subarray);
    const max = Math.max(...subarray);

    left = findBoundary(
      array,
      left,
      (index, arr) => index > 0 && arr[index - 1] > min,
      -1,
    );
    right = findBoundary(
      array,
      right,
      (index, arr) => index < arr.length - 1 && arr[index + 1] < max,
      1,
    );

    return [left, right];
  };
})();
