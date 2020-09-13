class Solution:
    def func(self, nums):
        """
        摩尔投票

        Args:
            nums: list[int]
        
        Return:
            int
        """
        res = None
        votes = 0

        for num in nums:
            if votes == 0:
                res = num
            if num == res:
                votes += 1
            else:
                votes -= 1
        return res


if __name__ == "__main__":
    nums = list(map(int, input().split()))
    print(Solution().func(nums))