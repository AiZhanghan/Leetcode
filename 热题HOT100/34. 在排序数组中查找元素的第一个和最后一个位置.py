from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        """二分查找"""
        if not nums:
            return [-1, -1]
        left = 0
        right = len(nums) - 1
        # 找左边界
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] >= target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
        # 不存在目标值
        if left >= len(nums) or nums[left] != target:
            return [-1, -1]
        res = [left]
        # 找右边界
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] <= target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
        res.append(right)
        return res
