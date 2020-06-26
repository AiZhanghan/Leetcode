class Solution:
    def containsDuplicate(self, nums):
        """
        Args:
            nums: list[int]
        
        Return:
            bool
        """
        visited = set()
        for num in nums:
            if num in visited:
                return True
            visited.add(num)
        return False