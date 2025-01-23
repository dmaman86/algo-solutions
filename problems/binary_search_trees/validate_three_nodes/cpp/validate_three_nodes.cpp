#include "validate_three_nodes.h"

bool validateThreeNodes(BST *nodeOne, BST *nodeTwo, BST *nodeThree) {

  auto isAncestor = [](BST *ancestor, BST *node) -> bool {
    while (ancestor) {
      if (ancestor == node)
        return true;
      ancestor =
          (node->value < ancestor->value) ? ancestor->left : ancestor->right;
    }
    return false;
  };

  auto isDescendant = [&isAncestor](BST *node, BST *descendant) -> bool {
    return isAncestor(node, descendant);
  };

  bool isNodeOneAncestorOfTwo = isAncestor(nodeOne, nodeTwo);
  bool isNodeThreeAncestorOfTwo = isAncestor(nodeThree, nodeTwo);

  if (isNodeOneAncestorOfTwo)
    return isDescendant(nodeTwo, nodeThree);
  if (isNodeThreeAncestorOfTwo)
    return isDescendant(nodeTwo, nodeOne);
  return false;
}
