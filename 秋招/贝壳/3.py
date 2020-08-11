class Solution:
    def func(self, n):
        """
        Args:
            n: int
        
        Return:
            int
        """
        n_bin = bin(n)
        return len(n_bin) - 2   


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        print(Solution().func(n))
