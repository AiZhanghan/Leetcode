class Solution:
    def minNumber(self, nums):
        """
        Args:
            nums: list[int]
        
        Return:
            str
        """
        self.quick_sort(nums, 0, len(nums) - 1)

        return "".join(map(str, nums))
    
    def quick_sort(self, nums, start, end):
        """
        Args:
            nums: list[int]
            start: int
            end: int
        """
        if start >= end:
            return
        
        pivot_index = self.partition(nums, start, end)
        self.quick_sort(nums, start, pivot_index - 1)
        self.quick_sort(nums, pivot_index + 1, end)

    def partition(self, nums, start, end):
        """
        Args:
            nums: list[int]
            start: int
            end: int
        
        Return:
            int
        """
        

        pivot = nums[end]
        # [start, i) <= pivot
        i = start
        for j in range(start, end):
            if str(nums[j]) + str(pivot) <= str(pivot) + str(nums[j]):
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
        nums[i], nums[end] = nums[end], nums[i]
        return i


if __name__ == "__main__":
    nums = [3,30,34,5,9]
    print(Solution().minNumber(nums))