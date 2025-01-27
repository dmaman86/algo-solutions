#include <vector>

class AncestralTree {
public:
  char name;
  AncestralTree *ancestor;

  AncestralTree(char name) {
    this->name = name;
    this->ancestor = nullptr;
  }

  void addAsAncestor(std::vector<AncestralTree *> descendants) {
    for (AncestralTree *descendant : descendants) {
      descendant->ancestor = this;
    }
  }
};

int getDepth(AncestralTree *, AncestralTree *);
AncestralTree *backtrackAncestor(AncestralTree *, int, int);
AncestralTree *getYoungestCommonAncestor(AncestralTree *, AncestralTree *,
                                         AncestralTree *);
