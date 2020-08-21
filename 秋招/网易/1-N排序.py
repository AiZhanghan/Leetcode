import random


class Solution:
    def sort(self, nums):
        """
        Args:
            nums: list[int]
        """
        for i in range(len(nums)):
            while nums[i] != i + 1:
                temp = nums[nums[i] - 1]
                nums[nums[i] - 1] = nums[i]
                nums[i] = temp
            


if __name__ == "__main__":
    n = 10
    nums = [x for x in range(1, n + 1)]
    random.shuffle(nums)
    print(nums)
    Solution().sort(nums)
    print(nums)
