class Solution:
    def constructArr(self, a):
        """
        Args:
            a: list[int]
        
        Return:
            list[int]
        """
        b = [1 for _ in range(len(a))]
        tmp = 1
        for i in range(1, len(a)):
            b[i] = b[i - 1] * a[i - 1]
        for i in range(len(a) - 2, -1, -1):
            tmp *= a[i + 1]
            b[i] *= tmp
        return b