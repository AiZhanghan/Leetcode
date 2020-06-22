class Solution:
    def dailyTemperatures(self, T):
        """
        Args:
            T: list[int]
        
        Return:
            list[int]
        """
        res = [0 for _ in range(len(T))]
        for i in reversed(range(len(T) - 1)):
            j = i + 1
            while j < len(T):
                if T[j] > T[i]:
                    res[i] = j - i
                    break
                elif res[j] == 0:
                    res[i] = 0
                    break
                j += res[j]
        return res


# class Solution:
#     def dailyTemperatures(self, T):
#         """
#         Args:
#             T: list[int]
        
#         Return:
#             list[int]
#         """
#         res = [0 for _ in range(len(T))]
#         s = []
#         for i in range(len(T)):
#             while s and T[i] > T[s[-1]]:
#                 t = s.pop()
#                 res[t] = i - t
#             s.append(i)
#         return res


# class Solution:
#     def dailyTemperatures(self, T):
#         """
#         Args:
#             T: list[int]
        
#         Return:
#             list[int]
#         """
#         dp = [0 for _ in range(len(T))]
#         visited = {T[-1]: len(T) - 1}
#         for i in reversed(range(len(T) - 1)):
#             t = T[i]
#             j = len(T)
#             for key, value in visited.items():
#                 if key > t:
#                     j = min(j, value)
#             if j == len(T):
#                 dp[i] = 0
#             else:
#                 dp[i] = j - i
#             visited[t] = i
#         return dp


# class Solution:
#     def dailyTemperatures(self, T):
#         """
#         Args:
#             T: list[int]
        
#         Return:
#             list[int]
#         """
#         dp = [0 for _ in range(len(T))]
#         for i in reversed(range(len(T) - 1)):
#             j = i + 1
#             while j < len(T) and T[i] >= T[j]:
#                 j += 1
#             if j == len(T):
#                 dp[i] = 0
#             else:
#                 dp[i] = j - i
#         return dp