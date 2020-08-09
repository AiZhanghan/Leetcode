class Solution:
    def can_cutting(self, nums):
        """滑动窗口

        Args:
            nums: list[int]
        
        Return:
            bool
        """
        target = sum(nums) / 2
        left = 0
        state = 0
        res = False

        for right in range(len(nums)):
            state += nums[right]
            while state > target:
                state -= nums[left]
                left += 1
            if state == target:
                res = True
                break

        return res    


if __name__ == "__main__":
    T = int(input())
    s = Solution()
    for _ in range(T):
        _ = int(input())
        nums = list(map(int, input().split()))
        if s.can_cutting(nums):
            print("YES")
        else:
            print("NO")
