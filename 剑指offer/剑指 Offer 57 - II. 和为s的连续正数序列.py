from collections import deque


class Solution:
    def findContinuousSequence(self, target):
        """
        Args:
            target: int
        
        Return；
            list[list[int]]
        """
        res = []
        queue = deque()
        state = 0
        # l = 0
        for r in range(1, target // 2 + 2):
            state += r
            queue.append(r)
            while state > target:
                state -= queue.popleft()
            if state == target:
                res.append(list(queue))
        return res
