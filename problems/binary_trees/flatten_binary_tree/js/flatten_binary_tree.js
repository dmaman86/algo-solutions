export const flattenBinaryTree = (() => {
  const flattenInOrder = (node, state) => {
    if (!node) return;

    // traverse left subtree
    flattenInOrder(node.left, state);

    // store the head of the linked list
    if (!state.head) state.head = node;
    // link the previous node with the current node
    if (state.prev) {
      state.prev.right = node;
      node.left = state.prev;
    }
    // update the previous node
    state.prev = node;

    // traverse right subtree
    flattenInOrder(node.right, state);
  };

  return (root) => {
    const state = { prev: null, head: null };
    flattenInOrder(root, state);

    return state.head;
  };
})();
