export const allKindsOfNodeDepths = (() => {
  let result = 0;

  const preorderTraversal = (node) => {
    if (!node) return { depthSum: 0, size: 0 }; // depth sum = 0, size = 0 for null nodes

    // recursive calls for left and right subtrees
    const { depthSum: leftDepthSum, size: leftSize } = preorderTraversal(
      node.left,
    );
    const { depthSum: rightDepthSum, size: rightSize } = preorderTraversal(
      node.right,
    );

    // calculate depth sum and size for the current node
    const depthSum = leftDepthSum + rightDepthSum;
    const size = leftSize + rightSize + 1;

    // calculate the global result with the depth sum for this subtree
    result += depthSum;

    // return the depth sum including the current node and its size
    return { depthSum: depthSum + size, size };
  };

  return (root) => {
    result = 0; // reset the global result for each call
    preorderTraversal(root);
    return result;
  };
})();
