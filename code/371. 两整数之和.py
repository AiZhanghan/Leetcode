class Solution:
    def getSum(self, a, b):
        """
        Args:
            a: int
            b: int
        
        Return:
            int
        """
        MASK = 0x100000000
        MAX_INT = 0x7FFFFFFF
        MIN_INT = MAX_INT + 1
        while b:
            carry = (a & b) << 1
            a = (a ^ b) % MASK
            b = carry % MASK

        return a if a <= MAX_INT else ~((a % MIN_INT) ^ MAX_INT) 


if __name__ == "__main__":
    a, b = 10, 23
    print(Solution().getSum(a, b))