class Solution:
    def func(self, nums):
        """
        Args:
            nums: list[int]
        
        Return:
            list[int]
        """
        nums_sorted = sorted(nums)
        mid_index = len(nums) // 2
        mid1 = nums_sorted[mid_index - 1]
        mid2 = nums_sorted[mid_index]

        res = []

        for num in nums:
            if num <= mid1:
                res.append(mid2)
            else:
                res.append(mid1)
        return res


if __name__ == "__main__":
    n = int(input())
    nums = list(map(int, input().split()))
    res = Solution().func(nums)
    for x in res:
        print(x)