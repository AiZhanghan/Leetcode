class Solution:
    def threeSumClosest(self, nums, target):
        """
        Args：
            nums: list[int]
            target: int
        
        Return:
            int
        """
        nums.sort()
        res = nums[0] + nums[1] + nums[2]
        for i in range(len(nums) - 2):
            j = i + 1
            k = len(nums) - 1
            while j < k:
                cur_sum = nums[i] + nums[j] + nums[k]
                if abs(cur_sum - target) < abs(res - target):
                    res = cur_sum
                if cur_sum > target:
                    k -= 1
                elif cur_sum < target:
                    j += 1
                else:
                    return target
        return res