import math


class Solution:
    def eat_grapes(self, grapes):
        """
        Args:
            grapes: list[int]
        
        Return:
            int
        """
        return max(math.ceil(sum(grapes) / 3), math.ceil(max(grapes) / 2))


# class Solution:
#     def eat_grapes(self, grapes):
#         """
#         Args:
#             grapes: list[int]
        
#         Return:
#             int
#         """
#         a, b, c = sorted(grapes)
#         if a + b <= c // 2:
#             res = c // 2
#             if c % 2 != 0:
#                 res += 1
#         else:
#             res = sum(grapes) // 3 
#             if sum(grapes) % 3 != 0:
#                 res += 1
#         return res


if __name__ == "__main__":
    T = int(input())
    s = Solution()
    for _ in range(T):
        grapes = list(map(int, input().split()))
        print(s.eat_grapes(grapes))
    # print(s.eat_grapes([3, 8, 9]))