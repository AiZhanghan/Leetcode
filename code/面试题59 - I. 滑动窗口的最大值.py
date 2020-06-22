from collections import deque


class Solution:
    def maxSlidingWindow(self, nums, k):
        """单调双向队列
        
        Args:
            nums: List[int]
            k: int

        Return: List[int]
        """
        res = []
        q = deque()
        for i in range(len(nums)):
            while q and nums[i] >= nums[q[-1]]:
                q.pop()
            q.append(i)
            if q[0] == i - k:
                q.popleft()
            if i >= k - 1:
                res.append(nums[q[0]])
        return res

if __name__ == "__main__":
    nums = [1,3,-1,-3,5,3,6,7]
    k = 3
    print(Solution().maxSlidingWindow(nums, k))
