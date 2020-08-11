# class Solution:
#     def __init__(self, bound):
#         temp = [True for _ in range(bound + 1)]
#         self.prime = []
#         for i in range(2, len(temp)):
#             if temp[i]:
#                 self.prime.append(i)
#                 for j in range(i + i, len(temp), i):
#                     temp[j] = False

#     def func(self, N, M):
#         """
#         Args:
#             N: int
#             M: int
        
#         Return:
#             int
#         """
#         if N == 1 and M == 1:
#             return 1
#         size = N * M
#         for i in self.prime:
#             if size % i == 0:
#                 return i


# if __name__ == "__main__":
#     T = int(input())
#     bound = 10 ** 8
#     s = Solution(bound)
#     # s = Solution()
#     for _ in range(T):
#         N, M = list(map(int, input().split()))
#         print(s.func(N, M))


class Solution:
    def func(self, N, M):
        """
        Args:
            N: int
            M: int
        
        Return:
            int
        """
        if N == 1 and M == 1:
            return 1
        size = N * M
        for i in range(2, min(N, M) + 1):
            if size % i == 0:
                return i


if __name__ == "__main__":
    T = int(input())
    s = Solution()
    for _ in range(T):
        N, M = list(map(int, input().split()))
        print(s.func(N, M)) 


# class Solution:
#     def __init__(self, bound):
#         temp = [True for _ in range(bound + 1)]
#         self.prime = []
#         for i in range(2, len(temp)):
#             if temp[i]:
#                 self.prime.append(i)
#                 for j in range(i + i, len(temp), i):
#                     temp[j] = False

#     def func(self, N, M):
#         """
#         Args:
#             N: int
#             M: int
        
#         Return:
#             int
#         """
#         if N == 1 and M == 1:
#             return 1
#         size = N * M
#         for i in self.prime:
#             if size % i == 0:
#                 return i


# if __name__ == "__main__":
#     T = int(input())
#     args = []
#     bound = 0
#     for _ in range(T):
#         N, M = list(map(int, input().split()))
#         bound = max(bound, min(N, M))
#         args.append([N, M])
    
#     s = Solution(bound)
#     for N, M in args:
#         print(s.func(N, M))