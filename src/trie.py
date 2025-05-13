class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for c in word:
            node = node.children.setdefault(c, TrieNode())
        node.is_end_of_word = True

    def suggest(self, prefix):
        def dfs(node, prefix, results):
            if node.is_end_of_word:
                results.append(prefix)
            for c, n in node.children.items():
                dfs(n, prefix + c, results)

        node = self.root
        for c in prefix:
            if c in node.children:
                node = node.children[c]
            else:
                return []
        results = []
        dfs(node, prefix, results)
        return results
