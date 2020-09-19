class Solution:
    def isStraight(self, nums):
        """
        Args:
            nums: list[int]
        
        Return:
            bool
        """
        
        _min = 14
        _max = -1
        visited = set()
        for num in nums:
            if num == 0:
                continue
            elif num in visited:
                return False
            else:
                visited.add(num)
                _min = min(_min, num)
                _max = max(_max, num)
        return _max - _min < 5
