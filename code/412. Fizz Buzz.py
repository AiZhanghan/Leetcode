class Solution:
    def fizzBuzz(self, n):
        """
        Args:
            n: int
        
        Return:
            list[str]
        """
        res = [str(x) for x in range(1, n + 1)]
        for i in range(2, n, 3):
            res[i] = "Fizz"
        for i in range(4, n, 5):
            res[i] = "Buzz"
        for i in range(14, n, 15):
            res[i] = "FizzBuzz"
        return res