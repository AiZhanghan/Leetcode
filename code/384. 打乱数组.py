import random


class Solution:

    def __init__(self, nums):
        """
        Args:
            nums: list[int]
        """
        self.nums = nums

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        
        Return:
            list[int]
        """
        return self.nums

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        
        Return:
            list[int]
        """
        res = self.nums[:]
        for i in range(len(res)):
            j = random.randint(i, len(res) - 1)
            res[i], res[j] = res[j], res[i]
        return res


# class Solution:

#     def __init__(self, nums):
#         """
#         Args:
#             nums: list[int]
#         """
#         self.nums = nums

#     def reset(self):
#         """
#         Resets the array to its original configuration and return it.
        
#         Return:
#             list[int]
#         """
#         return self.nums

#     def shuffle(self):
#         """
#         Returns a random shuffling of the array.
        
#         Return:
#             list[int]
#         """
#         res = self.nums[:]
#         random.shuffle(res)
#         return res

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()