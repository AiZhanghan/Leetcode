class TrieNode:
    def __init__(self):
        self.R = 26
        self.links = [None for _ in range(self.R)]
        self.is_end = False

    def contains_key(self, ch):
        """
        Args:
            ch: str
        
        Return:
            bool
        """
        return self.links[ord(ch) - ord("a")] != None
    
    def get(self, ch):
        """
        Args:
            ch: str

        Return:
            TrieNode
        """
        return self.links[ord(ch) - ord("a")]
    
    def put(self, ch, node):
        """
        Args:
            ch: str
            node: TrieNode
        """
        self.links[ord(ch) - ord("a")] = node


class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        node = self.root
        for char in word:
            if not node.contains_key(char):
                node.put(char, TrieNode())
            node = node.get(char)
        node.is_end = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        node = self.search_prefix(word)
        return node != None and node.is_end

    def search_prefix(self, word: str) -> TrieNode:
        node = self.root
        for char in word:
            if node.contains_key(char):
                node = node.get(char)
            else:
                return
        return node

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        node = self.search_prefix(prefix)
        return node != None


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)