class Solution:
    def wiggleMaxLength(self, nums):
        """
        Args:
            nums: list[int]
        
        Return:
            int
        """
        if len(nums) < 2:
            return len(nums)
        
        count = 2 if nums[1] != nums[0] else 1
        pre_diff = nums[1] - nums[0]
        
        for i in range(2, len(nums)):
            diff = nums[i] - nums[i - 1]
            if diff > 0 and pre_diff <= 0 or diff < 0 and pre_diff >= 0:
                count += 1
                pre_diff = diff
        return count


if __name__ == "__main__":
    nums = [1,1,7,4,9,2,5]
    print(Solution().wiggleMaxLength(nums))