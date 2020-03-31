class Solution:
    def findRepeatNumber(self, nums):
        """
        parameter:
            nums: list[int]
        return: int
        """
        s = set()
        for num in nums:
            if num not in s:
                # O(1)
                s.add(num)
            else:
                return num
