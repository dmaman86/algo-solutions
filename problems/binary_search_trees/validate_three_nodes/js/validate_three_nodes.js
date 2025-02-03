export const validateThreeNodes = (() => {
  const isAncestor = (ancestor, node) => {
    if (!ancestor) return false;
    if (ancestor === node) return true;
    const nextNode =
      node.value < ancestor.value ? ancestor.left : ancestor.right;
    return isAncestor(nextNode, node);
  };

  return (nodeOne, nodeTwo, nodeThree) => {
    const isNodeOneAncestorOfTwo = isAncestor(nodeOne, nodeTwo);
    const isNodeThreeAncestorOfTwo = isAncestor(nodeThree, nodeTwo);

    if (!(isNodeOneAncestorOfTwo || isNodeThreeAncestorOfTwo)) return false;

    const nextPair = isNodeOneAncestorOfTwo
      ? [nodeTwo, nodeThree]
      : [nodeTwo, nodeOne];

    return isAncestor(...nextPair);
  };
})();
