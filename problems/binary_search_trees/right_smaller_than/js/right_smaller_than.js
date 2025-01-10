const createBST = () => {
  let root = null;

  class Node {
    constructor(value) {
      this.value = value;
      this.left = this.right = null;
      this.leftSize = 0;
    }
  }

  const insert = (value) => {
    if (!root) {
      root = new Node(value);
      return 0;
    }
    return _insert(root, value);
  };

  const _insert = (node, value) => {
    if (value <= node.value) {
      node.leftSize++;
      if (!node.left) {
        node.left = new Node(value);
        return 0;
      } else {
        return _insert(node.left, value);
      }
    } else {
      if (!node.right) {
        node.right = new Node(value);
        return node.leftSize + 1;
      } else {
        return node.leftSize + 1 + _insert(node.right, value);
      }
    }
  };
  return { insert };
};

export const rightSmallerThan = (array) => {
  const bst = createBST();
  const result = [];

  for (let i = array.length - 1; i >= 0; i--) {
    const count = bst.insert(array[i]);
    result.push(count);
  }
  return result.reverse();
};
