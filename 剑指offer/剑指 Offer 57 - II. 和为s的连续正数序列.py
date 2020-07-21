import collections


class Solution:
    def findContinuousSequence(self, target):
        """
        Args:
            target: int
        
        Return:
            list[list[int]]
        """
        res = []
        window = collections.deque()
        win_sum = 0

        for i in range(1, (target + 1) // 2 + 1):
            window.append(i)
            win_sum += i
            while win_sum > target:
                win_sum -= window.popleft()
            if win_sum == target and len(window) > 1:
                res.append(list(window))
        
        return res