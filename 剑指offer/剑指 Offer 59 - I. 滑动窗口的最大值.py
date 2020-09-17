from collections import deque


class Solution:
    def maxSlidingWindow(self, nums, k):
        """
        Args:
            nums: list[int]
            k: int
        
        Return:
            list[int]
        """
        res = []
        queue = deque()

        for r in range(len(nums)):
            while queue and queue[-1] < nums[r]:
                queue.pop()
            queue.append(nums[r])
            if r >= k - 1:
                l = r - k + 1
                if l > 0 and nums[l - 1] == queue[0]:
                    queue.popleft()
                res.append(queue[0])
        
        return res

