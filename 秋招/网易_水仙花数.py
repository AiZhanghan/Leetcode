class Solution:
    def print_daffodil(self):
        for num in range(100, 1000):
            if self.is_daffodil(num):
                print(num)
    
    def is_daffodil(self, num):
        """
        Args:
            num: int
        
        Return:
            bool
        """
        _sum = 0
        temp = num
        while temp:
            _sum += (temp % 10) ** 3
            temp //= 10
        return num == _sum


if __name__ == "__main__":
    Solution().print_daffodil()
