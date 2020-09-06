class Solution:
    def func(self, S):
        """
        Args:
            S: str
        
        Return:
            int
        """
        upper_count = 0
        for c in S:
            if c.isupper():
                upper_count += 1
        return abs(len(S) // 2 - upper_count)


if __name__ == "__main__":
    S = input()
    print(Solution().func(S))