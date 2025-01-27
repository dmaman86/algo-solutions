// IIFE to find the longest increasing subsequence in an array
export const longestIncreasingSubsequence = (() => {
  // Binary search to find the position to insert/replace
  const lowerBound = (array, target) => {
    let left = 0,
      right = array.length;
    while (left < right) {
      const mid = Math.floor((left + right) / 2);
      if (array[mid] < target) left = mid + 1;
      else right = mid;
    }
    return left;
  };

  // build LIS and result the last index and predecessors
  const buildLIS = (array) => {
    const lisValues = []; // tracks active LIS values
    const indices = []; // tracks indices of LIS elements
    const predecessors = Array(array.length).fill(-1); // tracks LIS predecessors

    for (let i = 0; i < array.length; i++) {
      const pos = lowerBound(lisValues, array[i]); // find position using binary search
      if (pos === lisValues.length) {
        // extend LIS
        if (indices.length) predecessors[i] = indices[indices.length - 1];
        indices.push(i);
        lisValues.push(array[i]);
      } else {
        // replace LIS element
        if (pos) predecessors[i] = indices[pos - 1];
        indices[pos] = i;
        lisValues[pos] = array[i];
      }
    }
    return [indices[indices.length - 1], predecessors];
  };

  return (array) => {
    if (!Array.isArray(array) || !array.length) return [];

    const [lastIndex, predecessors] = buildLIS(array);
    const result = [];
    let current = lastIndex;
    while (current !== -1) {
      result.push(array[current]);
      current = predecessors[current];
    }
    return result.reverse();
  };
})();
