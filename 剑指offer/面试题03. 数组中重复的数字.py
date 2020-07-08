class Solution:
    def findRepeatNumber(self, nums):
        """原地置换, 修改nums
        time: O(N)
        space: O(1)
        
        Args:
            nums: list[int]

        return: int
        """
        for i in range(len(nums)):
            while nums[i] != i:
                if nums[i] == nums[nums[i]]:
                    return nums[i]
                else:
                    nums[nums[i]], nums[i]  = nums[i], nums[nums[i]]
        return -1


# class Solution:
#     def findRepeatNumber(self, nums):
#         """Hash, 不修改nums
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
