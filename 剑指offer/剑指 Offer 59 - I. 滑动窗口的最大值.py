import collections


class Solution:
    def maxSlidingWindow(self, nums, k):
        """
        Args:
            nums: list[int]
            k: int
        
        Return:
            list[int]
        """
        if not nums or k == 0:
            return []

        queue = collections.deque()
        
        for i in range(k):
            while queue and queue[-1] < nums[i]:
                queue.pop()
            queue.append(nums[i])
        
        res = [queue[0]]

        for i in range(k, len(nums)):
            if queue[0] == nums[i - k]:
                queue.popleft()
            while queue and queue[-1] < nums[i]:
                queue.pop()
            queue.append(nums[i])
            res.append(queue[0])
        
        return res