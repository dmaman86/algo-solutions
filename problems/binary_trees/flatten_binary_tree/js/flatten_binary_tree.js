export class BinaryTree {
  constructor(value) {
    this.value = value;
    this.left = null;
    this.right = null;
  }
}

export const flattenBinaryTree = (() => {
  const flattenInOrder = (node, state) => {
    if (!node) return;

    // traverse left subtree
    flattenInOrder(node.left, state);

    // link the previous node with the current node
    if (state.prev) {
      state.prev.right = node;
      node.left = state.prev;
    }
    state.prev = node; // update the previous node

    // traverse right subtree
    flattenInOrder(node.right, state);
  };

  return (root) => {
    const state = { prev: null }; // shared state object
    flattenInOrder(root, state);

    // find the leftmost node
    let leftMost = root;
    while (leftMost.left) leftMost = leftMost.left;

    return leftMost;
  };
})();
