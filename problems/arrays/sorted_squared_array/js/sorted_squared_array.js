export const sortedSquaredArray = (array) => {
  return array.map((value) => value * value).sort((a, b) => a - b);
};
