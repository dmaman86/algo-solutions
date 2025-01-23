export const validateThreeNodes = (() => {
  const isAncestor = (ancestor, node) => {
    if (!ancestor) return false;
    if (ancestor === node) return true;
    const nextNode =
      node.value < ancestor.value ? ancestor.left : ancestor.right;
    return isAncestor(nextNode, node);
  };

  const isDescendant = (node, descendant) => isAncestor(node, descendant);

  return (nodeOne, nodeTwo, nodeThree) => {
    const isNodeOneAncestorOfTwo = isAncestor(nodeOne, nodeTwo);
    const isNodeThreeAncestorOfTwo = isAncestor(nodeThree, nodeTwo);

    if (isNodeOneAncestorOfTwo) return isDescendant(nodeTwo, nodeThree);
    if (isNodeThreeAncestorOfTwo) return isDescendant(nodeTwo, nodeOne);
    return false;
  };
})();
