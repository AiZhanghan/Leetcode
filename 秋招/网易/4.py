class Solution:
    def drop(self, nums):
        """
        Args:
            nums: list[int]
        
        Return:
            int
        """
        nums.sort()
        for i in range(nums):
            if self.can_split(nums, i, len(nums) - 1):
                return sum(nums[:i])
    
    def can_split(self, nums, start, end):
        target = sum(nums[start: end + 1])
        if target % 2:
            return False
        target //= 2

        left = start
        right = end
        while left <= right:
            



if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        n = int(input())
        nums = list(map(int, input().split()))
