from collections import defaultdict


class Solution:
    def maxProduct(self, words):
        """
        Args:
            words: list[str]
        
        Return:
            int
        """
        hashmap = defaultdict(int)
        bit_number = lambda ch: ord(ch) - ord("a")

        for word in words:
            bitmask = 0
            for ch in word:
                bitmask |= 1 << bit_number(ch)
            hashmap[bitmask] = max(hashmap[bitmask], len(word))
        
        res = 0
        for x in hashmap:
            for y in hashmap:
                if x & y == 0:
                    res = max(res, hashmap[x] * hashmap[y])
        return res
