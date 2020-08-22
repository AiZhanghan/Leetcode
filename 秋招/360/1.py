class Solution:
    def func(self, names):
        """
        Args:
            names: list[str]
        
        Return:
            int
        """
        res = 0
        for name in names:
            if len(name) > 10:
                continue
            i = 0
            while i < len(name):
                if not name[i].isalpha():
                    break
                i += 1
            if i == len(name):
                res += 1
        return res


if __name__ == "__main__":
    n = int(input())
    names = []
    for _ in range(n):
        names.append(input())
    res = Solution().func(names)
    print(res)
