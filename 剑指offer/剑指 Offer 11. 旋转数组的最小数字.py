class Solution:
    def minArray(self, numbers):
        """
        Args:
            numbers: list[int]
        
        Return:
            int
        """
        left = 0
        right = len(numbers) - 1
        while left < right:
            mid = left + (right - left) // 2
            if numbers[right] < numbers[mid]:
                left = mid + 1
            elif numbers[right] > numbers[mid]:
                right = mid
            else:
                right -= 1
        return numbers[left]