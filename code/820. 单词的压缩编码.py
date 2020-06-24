class Solution:
    def minimumLengthEncoding(self, words):
        """
        Args:
            list[str]
        
        Return:
            int
        """
        res = 0
        trie = Trie()
        words.sort(key=len, reverse=True)
        for word in words:
            res += trie.insert(word)
        return res


class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        """
        Args:
            word: str
        
        Return:
            int
        """
        cur = self.root
        is_new = False
        for i in reversed(range(len(word))):
            c = ord(word[i]) - ord("a")
            if cur.children[c] == None:
                is_new = True
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        
        return len(word) + 1 if is_new else 0


class TrieNode:
    def __init__(self):
        self.val = None
        self.children = [None for _ in range(26)]