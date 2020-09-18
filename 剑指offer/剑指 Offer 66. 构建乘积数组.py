class Solution:
    def constructArr(self, a):
        """
        Args:
            a: list[int]
        
        Return:
            list[int]
        """
        b = [1 for _ in range(len(a))]
        temp = 1
        for i in range(1, len(a)):
            b[i] = b[i - 1] * a[i - 1]
        for i in range(len(a) - 2, -1, -1):
            temp *= a[i + 1]
            b[i] *= temp
        return b