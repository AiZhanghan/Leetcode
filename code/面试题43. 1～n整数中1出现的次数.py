class Solution:
    def countDigitOne(self, n):
        """
        Args:
            n: int
        Return:
            int
        """
        if n <= 0:
            return 0
        s = str(n)
        high = int(s[0])
        pow_ = 10 ** (len(s) - 1)
        last = n - high * pow_
        if high == 1:
            return self.countDigitOne(pow_ - 1) + last + 1 + \
                   self.countDigitOne(last)
        else:
            return high * self.countDigitOne(pow_ - 1) + pow_ + \
                   self.countDigitOne(last)


if __name__ == "__main__":
    n = 12
    print(Solution().countDigitOne(n))
