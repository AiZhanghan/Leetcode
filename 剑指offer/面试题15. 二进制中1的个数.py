class Solution:
    def hammingWeight(self, n):
        """
        parameter:
            n: int
        return: int
        """
        res = 0
        while n:
            res += 1
            n &= n - 1
        return res
        

# class Solution:
#     def hammingWeight(self, n):
#         """
#         parameter:
#             n: int
#         return: int
#         """
#         count = 0
#         while n != 0:
#             count += n % 2
#             n //= 2
#         return count