export const twoNumberSum = (array, targetSum) => {
  let arr = [];
  for (const num of array) {
    const found = array.find(
      (element) => element + num === targetSum && element !== num,
    );

    if (found !== undefined) {
      arr.push(num, found);
      return arr;
    }
  }
  return [];
};
