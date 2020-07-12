class Solution:
    def verifyPostorder(self, postorder):
        """
        Args:
            postorder: list[int]
        
        Return:
            bool
        """
        self.postorder = postorder
        return self.verify_postorder(0, len(postorder) - 1)
    
    def verify_postorder(self, start, end):
        """
        Args:
            start: int
            end: int
        
        Return:
            bool
        """
        if start >= end:
            return True
        
        root = self.postorder[end]
        right_start = end
        for i in range(start, end):
            if self.postorder[i] > root:
                right_start = i
                break
        for i in range(right_start, end):
            if self.postorder[i] < root:
                return False
        
        return self.verify_postorder(start, right_start - 1) and \
            self.verify_postorder(right_start, end - 1)