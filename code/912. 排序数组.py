from collections import Counter


class Solution:
    def sortArray(self, nums):
        """
        Args:
            nums: list[int]
        
        Return:
            list[int]
        """
        _max = -50001
        _min = 50001
        for num in nums:
            _max = max(_max, num)
            _min = min(_min, num)

        counter = [0 for _ in range(_max - _min + 1)]
        for num in nums:
            counter[num - _min] += 1
        
        index = 0
        for num in range(_min, _max + 1):
            count = counter[num - _min]
            while count > 0:
                nums[index] = num
                count -= 1
                index += 1
        return nums


# class Solution:
#     def sortArray(self, nums):
#         """
#         Args:
#             nums: list[int]
        
#         Return:
#             list[int]
#         """
#         counter = Counter(nums)
#         res = [0 for _ in range(len(nums))]
#         index = 0
#         for key in sorted(counter):
#             res[index: index + counter[key]] = \
#                 [key for _ in range(counter[key])]
#             index += counter[key]
#         return res