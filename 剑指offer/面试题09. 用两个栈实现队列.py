class CQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []


    def appendTail(self, value):
        """
        parameter:
            value: int
        return: None
        """
        self.stack1.append(value)


    def deleteHead(self):
        """
        parameter: None
        return: int
        """
        if not self.stack2:
            if not self.stack1:
                res = -1
            else:
                while self.stack1:
                    self.stack2.append(self.stack1.pop())
                res = self.stack2.pop()
        else:
            res = self.stack2.pop()
        
        return res


# Your CQueue object will be instantiated and called as such:
# obj = CQueue()
# obj.appendTail(value)
# param_2 = obj.deleteHead()