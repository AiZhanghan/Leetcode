class Solution:
    def func(self, nums):
        """
        Args:
            nums: list[int]
        
        Return:
            list[int]
        """
        nums.sort()
        res = set()
        for i in range(len(nums) - 2):
            if nums[i] > 0:
                break

            j = i + 1
            k = len(nums) - 1
            while j < k:
                temp = nums[i] + nums[j] + nums[k]
                if temp < 0:
                    j += 1
                elif temp > 0:
                    k -= 1
                else:
                    res.add((nums[i], nums[j], nums[k]))
                    j += 1
                    k -= 1
        res = list(res)
        res.sort()
        return res


if __name__ == "__main__":
    nums = list(map(int, input().split()))
    # nums = [-1, -1, 0, 0, 1, 1, 2, 2, -1, -1, -4]
    res = Solution().func(nums)
    for x, y, z in res:
        print(x, y, z)