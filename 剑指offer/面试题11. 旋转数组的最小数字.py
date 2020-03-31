class Solution:
    def minArray(self, numbers):
        """
        二分查找
        parameter:
            number: list[int]
        return: int
        """
        left = 0
        right = len(numbers) - 1

        while left != right:
            mid = (right + left) // 2
            if numbers[mid] < numbers[right]:
                # mid在右排序序列
                right = mid
            elif numbers[mid] > numbers[right]:
                # mid在左排序序列
                left = mid + 1
            else:
                right = right - 1

        return numbers[left]