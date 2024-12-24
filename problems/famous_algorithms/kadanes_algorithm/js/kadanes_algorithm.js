export const kadanesAlgorithm = (array) => {
  let maxSoFar = Number.MIN_SAFE_INTEGER;
  let maxEndingHere = 0;

  for (let i = 0; i < array.length; i++) {
    maxEndingHere += array[i];

    maxSoFar = Math.max(maxSoFar, maxEndingHere);

    if (maxEndingHere < 0) maxEndingHere = 0;
  }
  return maxSoFar;
};
