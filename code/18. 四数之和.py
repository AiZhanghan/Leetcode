class Solution:
    def fourSum(self, nums, target):
        """
        Args:
            nums: list[int]
            target: int
        
        Return:
            list[list[int]]
        """
        nums.sort()
        res = []
        for i in range(len(nums) - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, len(nums) - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                left = j + 1
                right = len(nums) - 1
                while left < right:
                    temp = nums[i] + nums[j] + nums[left] + nums[right]
                    if temp < target:
                        left += 1
                    elif temp > target:
                        right -= 1
                    else:
                        res.append([nums[i], nums[j], nums[left], nums[right]])
                        while left < right and nums[left + 1] == nums[left]:
                            left += 1
                        while left < right and nums[right - 1] == nums[right]:
                            right -= 1
                        left += 1
                        right -= 1
        return res


# class Solution:
#     def fourSum(self, nums, target):
#         """
#         Args:
#             nums: list[int]
#             target: int
        
#         Return:
#             list[list[int]]
#         """
#         res = set()
#         nums.sort()
#         for i in range(len(nums) - 3):
#             for j in range(i + 3, len(nums)):
#                 left = i + 1
#                 right = j - 1
#                 while left < right:
#                     temp = nums[i] + nums[j] + nums[left] + nums[right]
#                     if temp < target:
#                         left += 1
#                     elif temp > target:
#                         right -= 1
#                     else:
#                         res.add((nums[i], nums[left], nums[right], nums[j]))
#                         left += 1
#                         right -= 1
#         return [list(x) for x in res]


if __name__ == "__main__":
    nums = [1,0,-1,0,-2,2]
    target = 0
    print(Solution().fourSum(nums, target))