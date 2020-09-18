from random import shuffle
import heapq


class Solution:
    def getLeastNumbers(self, arr, k):
        """
        Args；
            arr: list[int]
            k: int
        
        Return:
            list[int]
        """
        if k == 0 or len(arr) == 0:
            return []
        pq = []
        for x in arr:
            if len(pq) < k:
                heapq.heappush(pq, -x)
            elif x < -pq[0]:
                heapq.heappop(pq)
                heapq.heappush(pq, -x)
        return [-x for x in pq]
                


# class Solution:
#     def getLeastNumbers(self, arr, k):
#         """
#         Args；
#             arr: list[int]
#             k: int
        
#         Return:
#             list[int]
#         """
#         if k == 0:
#             return []
#         shuffle(arr)
#         k -= 1
#         start = 0
#         end = len(arr) - 1
#         pivot_index = self.partition(arr, start, end)
#         while pivot_index != k:
#             if pivot_index < k:
#                 start = pivot_index + 1
#             else:
#                 end = pivot_index - 1
#             pivot_index = self.partition(arr, start, end)
#         return arr[: k + 1]
    
#     def partition(self, arr, start, end):
#         """
#         Args:
#             arr: list[int]
#             start: int
#             end: int
        
#         Return:
#             int
#         """
#         if start == end:
#             return start
#         # [start, i) <= pivot
#         pivot = arr[end]
#         i = start
        
#         for j in range(start, end):
#             if arr[j] <= pivot:
#                 arr[i], arr[j] = arr[j], arr[i]
#                 i += 1
#         arr[i], arr[end] = arr[end], arr[i]
#         return i