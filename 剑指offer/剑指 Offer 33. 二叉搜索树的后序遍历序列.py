class Solution:
    def verifyPostorder(self, postorder):
        """
        Args:
            postorder: list[int]
        
        Return:
            bool
        """
        return self.verify_postorder(postorder, 0, len(postorder) - 1)
    
    def verify_postorder(self, postorder, start, end):
        """
        Args:
            postorder: list[int]
            start: int
            end: int
        
        Return:
            bool
        """
        if start >= end:
            return True
        
        # 右子树位置
        right_start = start
        while right_start < end and postorder[right_start] < postorder[end]:
                right_start += 1

        for i in range(right_start, end):
            if postorder[i] <= postorder[end]:
                return False
        
        return self.verify_postorder(postorder, start, right_start - 1) \
            and self.verify_postorder(postorder, right_start, end - 1)
        
            