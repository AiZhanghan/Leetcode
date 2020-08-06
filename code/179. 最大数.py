import functools


class LargerNumKey(str):
    def __lt__(self, other):
        return self + other > other + self


class Solution:
    def largestNumber(self, nums):
        """
        Args:
            nums: list[int]
        
        Return:
            str
        """
        largest_num = "".join(sorted(map(str, nums), 
            key=functools.cmp_to_key(self.helper)))
        return "0" if largest_num[0] == "0" else largest_num
    
    @staticmethod
    def helper(x, y):
        """
        Args:
            x: str
            y: str
        
        Return:
            int
        """
        if x + y > y + x:
            return -1
        elif x + y < y + x:
            return 1
        else:
            return 0