from collections import Counter


class Solution:
    def func(self, nums):
        """
        Args:
            n: int
            nums: list[int]
        
        Return:
            bool
        """
        if not nums:
            return True
        nums.sort()
        leaf_count = 0
        for num in nums:
            if num == 1:
                leaf_count += 1
            elif num == 2 or num - 1 > leaf_count:
                return False
            else:
                leaf_count = leaf_count - num + 2
        return leaf_count == 1
            

if __name__ == "__main__":
    while input():
        nums = list(map(int, input().split()))
        res = Solution().func(nums)
        if res:
            print("YES")
        else:
            print("NO")
    # nums = [1, 1, 1, 1, 1, 1, 3, 3, 3, 3, 3, 3]
    # print(Solution().func(nums))