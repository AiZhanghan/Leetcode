class Solution:
    def has_same_region(self, locations):
        """
        Args:
            locations: list[int]
        
        Return:
            bool
        """
        locations.sort()
        for i in range(1, len(locations)):
            if locations[i] == locations[i - 1]:
                return False
        return True