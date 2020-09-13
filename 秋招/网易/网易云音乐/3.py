class Solution:
    def func(self, nums, X):
        """
        Args:
            nums: list[int]
            X: int
        
        Return:
            int
        """
        if not nums:
            return 0

        res = 0
        nums.sort()
        
        left = 0
        right = len(nums) - 1
        while left < right:
            temp = nums[left] + nums[right]
            if temp <= X:
                left += 1
            right -= 1
            res += 1
        
        if left == right:
            res += 1
        
        return res


if __name__ == "__main__":
    X = int(input())
    nums = list(map(int, input().split()))
    print(Solution().func(nums, X))