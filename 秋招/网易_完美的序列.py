class Solution:
    def perfect_sequence(self, nums):
        """
        Args:
            nums: list[int]
        
        Return:
            int
        """
        count = 1
        res = 1
        _sum = nums[0]
        for i in range(1, len(nums)):
            if nums[i] >= _sum:
                count += 1
                res = max(res, count)
            else:
                count = 1
                _sum = 0
            _sum += nums[i]
        return res


if __name__ == "__main__":
    
    T = int(input())
    s = Solution()
    for _ in range(T):
        _ = int(input())
        nums = list(map(int, input().split()))
        print(s.perfect_sequence(nums))

    # nums = [1, 3, 9, 2, 6]
    # nums = [4, 2, 9, 16, 7]
    # print(Solution().perfect_sequence(nums))
