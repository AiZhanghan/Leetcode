class Solution:
    def findNthDigit(self, n):
        """
        Args:
            n: int
        
        Return:
            int
        """
        digit = 1
        start = 1
        count = 9
        while n > count:
            n -= count
            start *= 10
            digit += 1
            count = 9 * start * digit
        num = start + (n - 1) // digit
        return int(str(num)[(n - 1) % digit])
