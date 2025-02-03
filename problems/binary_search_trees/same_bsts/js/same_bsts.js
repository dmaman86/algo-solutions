export const sameBsts = (() => {
  const getChildren = (array) => {
    const smaller = [];
    const greater_or_equal = [];

    for (let i = 1; i < array.length; i++) {
      if (array[i] < array[0]) {
        smaller.push(array[i]);
      } else {
        greater_or_equal.push(array[i]);
      }
    }
    return { smaller, greater_or_equal };
  };

  return (arrayOne, arrayTwo) => {
    if (!arrayOne.length && !arrayTwo.length) return true;

    if (arrayOne.length !== arrayTwo.length || arrayOne[0] !== arrayTwo[0])
      return false;

    const { smaller: leftOne, greater_or_equal: rightOne } =
      getChildren(arrayOne);
    const { smaller: leftTwo, greater_or_equal: rightTwo } =
      getChildren(arrayTwo);

    return sameBsts(leftOne, leftTwo) && sameBsts(rightOne, rightTwo);
  };
})();
