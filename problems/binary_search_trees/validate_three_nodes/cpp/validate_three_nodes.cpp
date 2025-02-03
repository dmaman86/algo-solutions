#include "validate_three_nodes.h"
#include <functional>

bool validateThreeNodes(BST *nodeOne, BST *nodeTwo, BST *nodeThree) {

  std::function<bool(BST *, BST *)> isAncestor = [&](BST *ancestor,
                                                     BST *node) -> bool {
    if (!ancestor)
      return false;
    if (ancestor == node)
      return true;
    ancestor =
        (node->value < ancestor->value) ? ancestor->left : ancestor->right;
    return isAncestor(ancestor, node);
  };

  bool isNodeOneAncestorOfTwo = isAncestor(nodeOne, nodeTwo);
  bool isNodeThreeAncestorOfTwo = isAncestor(nodeThree, nodeTwo);

  if (!(isNodeOneAncestorOfTwo || isNodeThreeAncestorOfTwo))
    return false;

  BST *secondNode = isNodeOneAncestorOfTwo ? nodeThree : nodeOne;
  return isAncestor(nodeTwo, secondNode);
}
