class Solution:
    def minimum_digit_sum(self, x):
        """
        Args:
            x: int
        
        Return:
            str
        """
        res = ""
        n = x // 9
        m = x % 9
        if m != 0:
            res = str(m)
        res += "9" * n
        return res


# class Solution:
#     def minimum_digit_sum(self, x):
#         """
#         Args:
#             x: int
        
#         Return:
#             int
#         """
#         count9 = x // 9
#         res = (x - count9 * 9 + 1) * (10 ** count9) - 1
#         return res


if __name__ == "__main__":
    T = int(input())
    solution = Solution()
    for _ in range(T):
        x = int(input())
        print(solution.minimum_digit_sum(x))
