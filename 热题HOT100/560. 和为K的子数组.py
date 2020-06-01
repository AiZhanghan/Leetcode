class Solution:
    def subarraySum(self, nums, k):
        """
        Args:
            nums: list[int]
            k: int
        
        Return:
            int
        """
        res = 0
        dic = {0: 1}
        acc_sum = 0
        
        for num in nums:
            acc_sum += num
            res += dic.get(acc_sum - k, 0)
            dic[acc_sum] = dic.get(acc_sum, 0) + 1
        
        return res


if __name__ == "__main__":
    nums = [1, 1, 1]
    k = 2
    print(Solution().subarraySum(nums, k))