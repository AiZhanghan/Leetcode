class Solution:
    def validateStackSequences(self, pushed, popped):
        """
        Args:
            pushed: list[int]
            popped: list[int]
        
        Return:
            bool
        """
        stack = []
        push_index = 0
        for pop_val in popped:
            while not stack or stack[-1] != pop_val:
                if push_index >= len(pushed):
                    return False
                stack.append(pushed[push_index])
                push_index += 1
            stack.pop()
        return True
        

if __name__ == "__main__":
    pushed = [1,2,3,4,5]
    popped = [4,5,3,2,1]
    print(Solution().validateStackSequences(pushed, popped))