class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

    def search_in_children(self, letter: str):
        return self.children.get(letter, None)


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str):
        current_node: TrieNode = self.root
        for char in word:
            if char not in current_node.children:
                current_node.children[char] = TrieNode()
            current_node = current_node.children[char]
        current_node.is_end_of_word = True


def boggleBoard(board: list[list[str]], words: list[str]) -> dict:
    found_words: dict[str, list[tuple[int, int]]] = {}

    trie: Trie = Trie()
    for word in words:
        trie.insert(word)

    rows, cols = len(board), len(board[0])

    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    visited: list[list[bool]] = [[False for _ in range(cols)] for _ in range(rows)]

    def dfs(
        position: tuple[int, int],
        node: TrieNode,
        path: list[tuple[int, int]],
        current_word: str,
    ) -> None:
        x, y = position
        if not (0 <= x < rows and 0 <= y < cols) or visited[x][y]:
            return

        child_node = node.search_in_children(board[x][y])
        if not child_node:
            return

        visited[x][y] = True
        path.append((x, y))
        current_word += board[x][y]

        if child_node.is_end_of_word and current_word not in found_words:
            found_words[current_word] = path[:]

        for dx, dy in directions:
            dfs((x + dx, y + dy), child_node, path, current_word)

        visited[x][y] = False
        path.pop()

    for i in range(rows):
        for j in range(cols):
            dfs((i, j), trie.root, [], "")

    return {"words": found_words}
