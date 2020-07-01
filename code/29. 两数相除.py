INT_MAX = 2 ** 31 - 1
INT_MIN = - 2 ** 31


class Solution:
    def divide(self, dividend, divisor):
        """
        Args:
            dividend: int
            divisor: int
        
        Return:
            int
        """
        if dividend == 0:
            return 0
        if divisor == 1:
            return dividend
        if divisor == -1:
            if dividend > INT_MIN:
                return -dividend
            else:
                return INT_MAX
        a = dividend
        b = divisor
        sign = 1
        if a > 0 and b < 0 or a < 0 and b > 0:
            sign = -1
        a = abs(a)
        b = abs(b)
        res = self.div(a, b)
        if sign > 0:
            return res if res < INT_MAX else INT_MAX
        else:
            return -res

    def div(self, a, b):
        """
        Args:
            a: int
            b: int
        
        Return:
            int
        """
        if a < b:
            return 0
        count = 1
        tb = b
        while tb + tb <= a:
            count += count
            tb += tb
        return count + self.div(a - tb, b)