class Trie:
    def __init__(self, *words):
        self.root = {}
        for word in words:
            self.add(word)

    def add(self, word):
        node = self.root
        for c in word:
            node = node.setdefault(c, {})
        node["_end_"] = {}

    def __contains__(self, word):
        node = self.root
        for c in word:
            if c not in node:
                return False
            node = node[c]
        return "_end_" in node

    def startswith(self, prefix):
        node = self.root
        for c in prefix:
            if c not in node:
                return False
            node = node[c]
        return True
