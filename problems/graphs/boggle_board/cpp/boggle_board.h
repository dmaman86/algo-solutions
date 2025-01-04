#include <string>
#include <unordered_map>
#include <vector>

using Board = std::vector<std::vector<char>>;
using List = std::vector<std::string>;

class TrieNode {
public:
  std::unordered_map<char, TrieNode *> children;
  bool isEndOfWord;

  TrieNode() : isEndOfWord(false) {}

  ~TrieNode() {
    for (auto &child : children) {
      delete child.second;
    }
  }

  TrieNode *getChild(char letter) {
    return children.count(letter) ? children[letter] : nullptr;
  }
};

class Trie {
private:
  TrieNode *root;

public:
  Trie() { root = new TrieNode(); }

  ~Trie() { delete root; }

  void insert(const std::string &word) {
    TrieNode *current = root;
    for (char letter : word) {
      if (!current->children.count(letter)) {
        current->children[letter] = new TrieNode();
      }
      current = current->children[letter];
    }
    current->isEndOfWord = true;
  }

  TrieNode *getRoot() { return root; }
};

List boggleBoard(Board &, List &);
