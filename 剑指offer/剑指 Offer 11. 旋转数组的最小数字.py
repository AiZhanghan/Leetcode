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
        while left <= right:
            mid = left + (right - left) // 2
            if numbers[mid] <= numbers[right]:
                right = mid - 1
            else:
                left = mid + 1
        return numbers[left]