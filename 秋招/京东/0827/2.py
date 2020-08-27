import math


class Solution:
    def func(self, num):
        """
        Args:
            num: int
        
        Return:
            int
        """
        num = int(str(num)[::-1])
        res = [0 for _ in range(int(math.log(num, 5)) + 1)]
        for i in reversed(range(len(res))):
            res[i] = num // 5 ** i
            num %= 5 ** i
        return int("".join(map(str, res[::-1])))


if __name__ == "__main__":
    n = int(input())
    print(Solution().func(n))