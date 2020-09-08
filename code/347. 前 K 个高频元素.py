import heapq
import collections


class Solution:
    def topKFrequent(self, nums, k):
        """
        Args:
            nums: list[int]
            k: int
        
        Return:
            list[int]
        """
        counter = collections.Counter(nums)
        pq = []
        for num in counter:
            if len(pq) < k:
                heapq.heappush(pq, (counter[num], num))
            elif counter[num] > pq[0][0]:
                heapq.heappop(pq)
                heapq.heappush(pq, (counter[num], num))
        return [x for _, x in pq]

        
# class Solution:
#     def topKFrequent(self, nums, k):
#         """dict + 排序
#         Args:
#             nums: list[int]
#             k: int
        
#         Return:
#             list[int]
#         """
#         dic = {}
#         for num in nums:
#             if num in dic:
#                 dic[num] += 1
#             else:
#                 dic[num] = 1
#         keys = list(dic.keys())
#         keys.sort(key=lambda x: dic[x], reverse=True)
#         return keys[:k]


# class Solution:
#     def topKFrequent(self, nums, k):
#         """Counter

#         Args:
#             nums: list[int]
#             k: int
        
#         Return:
#             list[int]
#         """
#         return [key for key, _ in collections.Counter(nums).most_common(k)]