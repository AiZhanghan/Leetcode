class Solution:
    def search(self, nums, target):
        """
        Args:
            nums: list[int]
            target: int
        
        Return:
            int
        """
        left = 0
        right = len(nums) - 1
        # 找左边界
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        l = left
        # 找右边界
        left = l
        right = len(nums) - 1
        while left <= right:
            mid = left + (right - left)
            if nums[mid] == target:
                left = mid + 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        r = right
        return r - l + 1