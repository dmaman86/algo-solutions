#include "youngest_common_ancestor.h"

int getDepth(AncestralTree *node, AncestralTree *topAncestor) {
  int depth = 0;
  while (node != topAncestor) {
    node = node->ancestor;
    depth++;
  }
  return depth;
};

AncestralTree *backtrackAncestor(AncestralTree *node, int currentDepth,
                                 int targetDepth) {
  while (currentDepth > targetDepth) {
    node = node->ancestor;
    currentDepth--;
  }
  return node;
}

AncestralTree *getYoungestCommonAncestor(AncestralTree *topAncestor,
                                         AncestralTree *descendantOne,
                                         AncestralTree *descendantTwo) {

  int depthOne = getDepth(descendantOne, topAncestor);
  int depthTwo = getDepth(descendantTwo, topAncestor);

  descendantOne = backtrackAncestor(descendantOne, depthOne, depthTwo);
  descendantTwo = backtrackAncestor(descendantTwo, depthTwo, depthOne);

  while (descendantOne != descendantTwo) {
    descendantOne = descendantOne->ancestor;
    descendantTwo = descendantTwo->ancestor;
  }
  return descendantOne;
}
