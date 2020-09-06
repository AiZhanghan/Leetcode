class Solution:
    def func(self, n, a):
        """
        Args:
            n: int
            a: list[int]
        """
        res = 0
        for i in range(1, n + 1):
            bi = a[i - 1]
            for j in range(1, n + 1):
                bi ^= i % j
            res ^= bi
        return res


if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    print(Solution().func(n, a))