class Solution:
    def fib(self, n):
        """
        Args:
            n: int

        Return: int
        """
        a, b = 0, 1
        for _ in range(n):
            a, b = b, a + b
        return a % 1000000007


if __name__ == "__main__":
    n = 1
    print(Solution().fib(n))