import random


class Solution:
    def wiggleSort(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        
        Args:
            nums: list[int]
        """
        random.shuffle(nums)
        mid_index = len(nums) // 2
        self.quick_select(nums, mid_index)
        mid = nums[mid_index]

        i = 0
        j = 0
        k = len(nums) - 1
        while j < k:
            if nums[j] > mid:
                nums[j], nums[k] = nums[k], nums[j]
                k -= 1
            elif nums[j] < mid:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j += 1
            else:
                j += 1

        if len(nums) % 2:
            mid_index += 1
        temp1 = nums[:mid_index]
        temp2 = nums[mid_index:]
        for i in range(len(temp1)):
            nums[2 * i] = temp1[-1-i]
        for i in range(len(temp2)):
            nums[2 * i + 1] = temp2[-1-i]
        # temp1 = nums[:mid_index][::-1]
        # temp2 = nums[mid_index:][::-1]
        # i = 0
        # j = 0
        # for k in range(len(nums)):
        #     if k % 2 == 0:
        #         nums[k] = temp1[i]
        #         i += 1
        #     else:
        #         nums[k] = temp2[j]
        #         j += 1

    def quick_select(self, nums, target):
        """
        Args:
            nums: list[int
            target: int
        """
        left = 0
        right = len(nums) - 1
        while True:
            index = self.partition(nums, left, right)
            if index == target:
                return
            elif index < target:
                left = index + 1
            else:
                right = index - 1
        
    def partition(self, nums, left, right):
        """
        Args:
            nums: list[int]
            left: int
            right: int
        """
        pivot = nums[right]
        i = left
        for j in range(left, right + 1):
            if nums[j] <= pivot:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
        return i - 1


# class Solution:
#     def wiggleSort(self, nums):
#         """
#         Do not return anything, modify nums in-place instead.
        
#         Args:
#             nums: list[int]
#         """
#         nums.sort()
#         A = nums[:(len(nums) + 1) // 2][::-1]
#         B = nums[len(A):][::-1]
#         j = 0
#         k = 0
#         for i in range(len(nums)):
#             if i % 2 == 0:
#                 nums[i] = A[j]
#                 j += 1
#             else:
#                 nums[i] = B[k]
#                 k += 1


if __name__ == "__main__":
    nums = [1,5,1,1,6,4]
    s = Solution()
    s.quick_select(nums, 3)