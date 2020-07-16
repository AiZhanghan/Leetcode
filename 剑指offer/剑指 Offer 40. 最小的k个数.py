import random
import heapq


class Solution:
    def getLeastNumbers(self, arr, k):
        """
        Args:
            arr: list[int]
            k: int
        
        Return:
            list[int]
        """
        return heapq.nsmallest(k, arr)


# class Solution:
#     def getLeastNumbers(self, arr, k):
#         """超时？

#         Args:
#             arr: list[int]
#             k: int
        
#         Return:
#             list[int]
#         """
#         if k == 0 or not arr:
#             return []

#         self.arr = arr[:]
#         random.shuffle(self.arr)
        
#         k = k - 1
#         j = self.partition(0, len(self.arr) - 1)
#         while j != k:
#             if j < k:
#                 j = self.partition(j + 1, len(arr) - 1)
#             else:
#                 j = self.partition(0, j - 1)
        
#         return self.arr[: j + 1]
    
#     def partition(self, lo, hi):
#         """
#         Args:
#             lo: int
#             hi: int
#         """
#         i = lo
#         j = hi + 1
#         pivot = self.arr[lo]
#         while True:
#             while i + 1 <= hi and self.arr[i + 1] < pivot:
#                 i += 1
#             i += 1
#             while j - 1 >= lo and self.arr[j - 1] > pivot:
#                 j -= 1
#             j -= 1
#             if i >= j:
#                 break
#             self.arr[i], self.arr[j] = self.arr[j], self.arr[i]
#         self.arr[lo], self.arr[j] = self.arr[j], self.arr[lo]
#         return j


if __name__ == "__main__":
    arr = [0,1,1,2,4,4,1,3,3,2]
    k = 6
    print(Solution().getLeastNumbers(arr, k))