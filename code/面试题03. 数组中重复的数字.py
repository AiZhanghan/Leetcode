class Solution:
    def findRepeatNumber(self, nums):
        """原地置换
        
        Args:
            nums: list[int]

        return: int
        """



# class Solution:
#     def findRepeatNumber(self, nums):
#         """
#         Hash, 不修改nums
#         time: O(N)
#         space: O(N)
        
#         Args:
#             nums: list[int]

#         return: int
#         """
#         visited = set()
#         for num in nums:
#             if num not in visited:
#                 # O(1)
#                 visited.add(num)
#             else:
#                 return num
        
#         return -1
