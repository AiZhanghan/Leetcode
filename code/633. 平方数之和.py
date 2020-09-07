import math


class Solution:
    def judgeSquareSum(self, c):
        """
        Args:
            c: int
        
        Return:
            bool
        """
        l = 0
        r = int(math.sqrt(c))
        while l <= r:
            temp = l ** 2 + r ** 2
            if temp < c:
                l += 1
            elif temp > c:
                r -= 1
            else:
                return True
        return False


if __name__ == "__main__":
    c = 4
    print(Solution().judgeSquareSum(c))