class Solution:
    def verifyPostorder(self, postorder):
        """
        Args:
            postorder: list[int]
        
        Return:
            bool
        """
        self.postorder = postorder
        return self._verify_postorder(0, len(postorder) - 1)
    
    def _verify_postorder(self, begin, end):
        """
        Args:
            begin: int
            end: int
        Return:
            bool
        """
        if begin >= end:
            return True
    
        # 确定左右子树范围
        right_begin = begin
        while self.postorder[right_begin] < self.postorder[end]:
            right_begin += 1

        for i in range(right_begin, end):
            if self.postorder[i] < self.postorder[end]:
                return False
        return self._verify_postorder(begin, right_begin - 1) and \
               self._verify_postorder(right_begin, end - 1)

    