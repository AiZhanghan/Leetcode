class Solution:
    def lenLongestFibSubseq(self, A):
        """暴力

        Args:
            A: list[int]
        
        Return: 
            int
        """
        dp = {}
        res = 0
        s = set(A)
        for i in range(2, len(A)):
            for j in range(i):
                diff = A[i] - A[j]
                if diff < A[j] and diff in s:
                    dp[(A[j], A[i])] = dp.get((diff, A[j]), 2) + 1
                    res = max(res, dp[(A[j], A[i])])
        return res


# class Solution:
#     def lenLongestFibSubseq(self, A):
#         """暴力

#         Args:
#             A: list[int]
        
#         Return: 
#             int
#         """
#         res = 0
#         s = set(A)
#         for i in range(len(A) - 2):
#             for j in range(i + 1, len(A) - 1):
#                 pre = A[i]
#                 cur = A[j]
#                 nxt = pre + cur
#                 count = 2
#                 while nxt in s:
#                     count += 1
#                     pre = cur
#                     cur = nxt
#                     nxt = pre + cur
#                 res = max(res, count)
#         return res if res > 2 else 0


# if __name__ == "__main__":
#     A = [1,2,3,4,5,6,7,8]
#     print(Solution().lenLongestFibSubseq(A))