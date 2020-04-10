"""太烦人 TODO"""


class Solution:
    def findNthDigit(self, n):
        """
        Args:
            n: int
        Return:
            int
        """
        # n的位数
        base = 9
        digits = 1
        temp = n
        while temp - base * digits > 0:
            temp -= base * digits
            base *= 10
            digits += 1
        pass
