export const repairBST = (tree) => {
  let first = null,
    second = null,
    prev = null;

  const inOrder = (node) => {
    if (!node) return;
    inOrder(node.left);
    if (prev && prev.value > node.value) {
      if (!first) {
        first = prev;
      }
      second = node;
    }
    prev = node;
    inOrder(node.right);
  };
  inOrder(tree);

  if (first && second) {
    [first.value, second.value] = [second.value, first.value];
  }
  return tree;
};
