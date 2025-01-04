const TrieNode = class {
  constructor() {
    this.children = {};
    this.isEndOfWord = false;
  }

  searchChild(character) {
    return this.children[character] || null;
  }
};

const Trie = class {
  constructor() {
    this.root = new TrieNode();
  }

  insert(word) {
    let currentNode = this.root;
    for (const char of word) {
      if (!currentNode.children[char])
        currentNode.children[char] = new TrieNode();
      currentNode = currentNode.children[char];
    }
    currentNode.isEndOfWord = true;
  }
};

export const boggleBoard = (board, words) => {
  const foundWords = [];
  const remainingWords = new Set(words);

  const trie = new Trie();
  for (const word of words) {
    trie.insert(word);
  }

  const rows = board.length;
  const cols = board[0].length;
  const directions = [
    [-1, -1],
    [-1, 0],
    [-1, 1],
    [0, -1],
    [0, 1],
    [1, -1],
    [1, 0],
    [1, 1],
  ];

  const visited = Array.from({ length: rows }, () => Array(cols).fill(false));

  const dfs = (position, node, path) => {
    const [x, y] = position;

    if (x < 0 || y < 0 || x >= rows || y >= cols || visited[x][y]) return;

    const childNode = node.searchChild(board[x][y]);
    if (!childNode) return;

    visited[x][y] = true;
    path.push(board[x][y]);

    if (childNode.isEndOfWord) {
      const word = path.join("");
      if (remainingWords.has(word)) {
        foundWords.push(word);
        remainingWords.delete(word);
        childNode.isEndOfWord = false;
      }
    }

    for (const [dx, dy] of directions) {
      dfs([x + dx, y + dy], childNode, path);
    }
    visited[x][y] = false;
    path.pop();
  };

  for (let i = 0; i < board.length; i++) {
    for (let j = 0; j < board[0].length; j++) {
      if (!remainingWords.size) break;
      dfs([i, j], trie.root, []);
    }
    if (!remainingWords.size) break;
  }
  return foundWords;
};
