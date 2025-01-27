export class AncestralTree {
  constructor(name) {
    this.name = name;
    this.ancestor = null;
  }

  addAsAncestor(descendants) {
    descendants.forEach((descendant) => {
      descendant.ancestor = this;
    });
  }
}

export const getYoungestCommonAncestor = (() => {
  const getDepth = (node, topAncestor) => {
    let depth = 0;
    while (node !== topAncestor) {
      depth++;
      node = node.ancestor;
    }
    return depth;
  };

  const backtrackAncestor = (node, currentDepth, targetDepth) => {
    while (currentDepth > targetDepth) {
      node = node.ancestor;
      currentDepth--;
    }
    return node;
  };

  return (topAncestor, descendantOne, descendantTwo) => {
    let depthOne = getDepth(descendantOne, topAncestor);
    let depthTwo = getDepth(descendantTwo, topAncestor);

    descendantOne = backtrackAncestor(descendantOne, depthOne, depthTwo);
    descendantTwo = backtrackAncestor(descendantTwo, depthTwo, depthOne);

    while (descendantOne !== descendantTwo) {
      descendantOne = descendantOne.ancestor;
      descendantTwo = descendantTwo.ancestor;
    }
    return descendantOne;
  };
})();
