#include <vector>

class Node {
public:
  int value, leftSize;
  Node *left, *right;

  Node(int value) : value(value), leftSize(0), left(nullptr), right(nullptr) {}

  ~Node() {
    delete left;
    delete right;
  }
};

class BST {
private:
  Node *root;
  int insert(Node *&, int);

public:
  BST() : root(nullptr) {}
  ~BST() { delete root; }
  int insert(int);
};

std::vector<int> rightSmallerThan(const std::vector<int> &);
