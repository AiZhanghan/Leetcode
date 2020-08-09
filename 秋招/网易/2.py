class Solution:
    def get_sushu(self, nums):
        """
        Args:
            nums: list[int]
        
        Return:
            int
        """
        res = 0
        for num in nums:
            res += num // 2
        return res


if __name__ == "__main__":
    n = int(input())
    nums = list(map(int, input().split()))
    s = Solution()
    print(s.get_sushu(nums))
    