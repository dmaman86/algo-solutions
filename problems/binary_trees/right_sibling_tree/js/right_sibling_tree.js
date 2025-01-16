export class BinaryTree {
  constructor(value) {
    this.value = value;
    this.left = null;
    this.right = null;
  }
}

export const rightSiblingTree = (() => {
  const helper = (node, parent, isLeft) => {
    if (!node) return;

    // store references to the left and right children before modifying them
    const left = node.left;
    const right = node.right;

    // recursively for the left subtree
    helper(left, node, true);

    // establish the right sibling connection
    if (!parent)
      node.right = null; // root node has no right sibling
    else if (isLeft)
      node.right = parent.right; // left child connects to parent's right child
    else {
      node.right = parent.right ? parent.right.left : null; // right child connects to left child of parent's right
    }
    // recursively for the right subtree
    helper(right, node, false);
  };

  return (root) => {
    helper(root, null, false); // start with no parent and isLeft = false
    return root;
  };
})();
