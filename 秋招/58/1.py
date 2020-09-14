from collections import Counter


class Solution:
    def func(self, s):
        """
        Args:
            s: str
        
        Return:
            list[tuple]
        """
        counter = Counter(s)
        res = list(counter.items())
        res.sort()
        return res


if __name__ == "__main__":
    s = input()
    res = Solution().func(s)
    for char, count in res:
        print("%s=%d" % (char, count), end=" ")
