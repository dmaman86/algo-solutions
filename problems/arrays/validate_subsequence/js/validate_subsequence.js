export const isValidSubsequence = (array, sequence) => {
  let index = 0;
  for (const value of array) {
    if (value === sequence[index]) index++;
    if (index === sequence.length) return true;
  }
  return false;
};
