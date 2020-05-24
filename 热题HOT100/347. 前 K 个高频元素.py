from collections import Counter


class Solution:
    def topKFrequent(self, nums, k):
        """dict + 排序
        Args:
            nums: list[int]
            k: int
        
        Return:
            list[int]
        """
        dic = {}
        for num in nums:
            if num in dic:
                dic[num] += 1
            else:
                dic[num] = 1
        keys = list(dic.keys())
        keys.sort(key=lambda x: dic[x], reverse=True)
        return keys[:k]


# class Solution:
#     def topKFrequent(self, nums, k):
#         """Counter

#         Args:
#             nums: list[int]
#             k: int
        
#         Return:
#             list[int]
#         """
#         return [key for key, _ in Counter(nums).most_common(k)]