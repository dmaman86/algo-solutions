export const maxPathSum = (() => {
  const maxPathSumHelper = (node, globalMax) => {
    if (!node) return 0;

    const left = Math.max(maxPathSumHelper(node.left, globalMax), 0);
    const right = Math.max(maxPathSumHelper(node.right, globalMax), 0);

    const localMax = left + right + node.value;

    globalMax.value = Math.max(globalMax.value, localMax);

    return node.value + Math.max(left, right);
  };

  return (tree) => {
    const globalMax = { value: -Infinity };
    maxPathSumHelper(tree, globalMax);
    return globalMax.value;
  };
})();
