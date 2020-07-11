class Solution:
    def exchange(self, nums):
        """
        Args:
            nums: list[int]
        
        Return:
            list[int]
        """
        res = nums[:]
        slow = 0
        for fast in range(len(res)):
            if res[fast] % 2 == 1:
                res[slow], res[fast] = res[fast], res[slow]
                slow += 1
            fast += 1
        return res
        

# class Solution:
#     def exchange(self, nums):
#         """
#         Args:
#             nums: list[int]
        
#         Return:
#             list[int]
#         """
#         left = 0
#         right = len(nums) - 1

#         res = nums[:]

#         while left < right:
#             while left < right and res[left] % 2 == 1:
#                 left += 1
#             while left < right and res[right] % 2 == 0:
#                 right -= 1
            
#             res[left], res[right] = res[right], res[left]
#             left += 1
#             right -= 1

#         return res