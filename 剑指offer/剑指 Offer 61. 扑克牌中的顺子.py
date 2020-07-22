class Solution:
    def isStraight(self, nums):
        """
        Args:
            nums: list[int]
        
        Return:
            bool
        """
        joker = 0
        nums.sort()
        for i in range(4):
            if nums[i] == 0:
                joker += 1
            elif nums[i] == nums[i + 1]:
                return False
        return nums[4] - nums[joker] < 5


# class Solution:
#     def isStraight(self, nums):
#         """
#         Args:
#             nums: list[int]
        
#         Return:
#             bool
#         """
#         visited = set()
#         ma, mi = 0, 14
#         for num in nums:
#             if num == 0:
#                 continue
#             if num in visited:
#                 return False
#             visited.add(num)
#             ma = max(ma, num)
#             mi = min(mi, num)
#         return ma - mi < 5


# class Solution:
#     def isStraight(self, nums):
#         """
#         Args:
#             nums: list[int]
        
#         Return:
#             bool
#         """
#         nums.sort()
#         clown = 0
        
#         i = 0
#         while i < len(nums) and nums[i] == 0:
#             clown += 1
#             i += 1
        
#         i += 1
#         while i < len(nums):
#             if nums[i] == nums[i - 1]:
#                 return False
#             clown = clown - (nums[i] - nums[i - 1] - 1)
#             if clown < 0:
#                 return False
#             i += 1
        
#         return True


# if __name__ == "__main__":
#     nums = [0,0,1,2,5]
#     print(Solution().isStraight(nums))
