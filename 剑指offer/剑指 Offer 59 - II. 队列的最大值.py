from collections import deque


class MaxQueue:

    def __init__(self):
        self.queue = deque()
        self.helper = deque()

    def max_value(self):
        """
        Return:
            int
        """
        if not self.helper:
            return -1
        else:
            return self.helper[0]

    def push_back(self, value):
        """
        Args:
            value: int
        """
        self.queue.append(value)
        while self.helper and self.helper[-1] < value:
            self.helper.pop()
        self.helper.append(value)

    def pop_front(self):
        """
        Return:
            int
        """
        if not self.queue:
            return -1
        res = self.queue.popleft()
        if self.helper[0] == res:
            self.helper.popleft()
        return res


# Your MaxQueue object will be instantiated and called as such:
# obj = MaxQueue()
# param_1 = obj.max_value()
# obj.push_back(value)
# param_3 = obj.pop_front()