export class BinaryTree {
  constructor(value) {
    this.value = value;
    this.left = null;
    this.right = null;
  }
}

export const compareLeafTraversal = (() => {
  const collectLeafNodes = (root, storedLeaf) => {
    if (!root) return;

    if (!root.left && !root.right) {
      storedLeaf.push(root.value);
    }
    collectLeafNodes(root.left, storedLeaf);
    collectLeafNodes(root.right, storedLeaf);
  };

  return (tree1, tree2) => {
    const leafTree1 = [];
    const leafTree2 = [];

    collectLeafNodes(tree1, leafTree1);
    collectLeafNodes(tree2, leafTree2);

    if (leafTree1.length !== leafTree2.length) return false;

    for (let i = 0; i < leafTree1.length; i++) {
      if (leafTree1[i] !== leafTree2[i]) return false;
    }
    return true;
  };
})();
