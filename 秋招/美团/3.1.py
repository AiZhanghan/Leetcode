class Solution:
    def func(self, n, a):
        """
        Args:
            n: int
            a: list[int]
        """
        res = 0
        for ai in a:
            res ^= ai
        
        for i in range(2, n + 1):
            shan, yushu = divmod(n, i)
            if shan % 2 == 0:
                for j in range(1, yushu + 1):
                    res ^= j
            else:
                for j in range(yushu + 1, i):
                    res ^= j
        
        return res


if __name__ == "__main__":
    # n = int(input())
    # a = list(map(int, input().split()))
    n = 7
    a = [1, 1, 1, 1, 1, 1, 1]
    print(Solution().func(n, a))