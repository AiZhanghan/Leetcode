class Solution:
    def maxChunksToSorted(self, arr):
        """
        Args:
            arr: list[int]
        
        Return:
            int
        """
        r = 0
        res = 0
        for i in range(len(arr)):
            r = max(r, arr[i])
            if r == i:
                res += 1

        return res