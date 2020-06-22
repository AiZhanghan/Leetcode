"""
1. 快速排序(选择)
2. 堆(nlargest)
"""


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
        if not arr or not k:
            return []
        heap = []
        for num in arr:
            if len(heap) < k:
                heapq.heappush(heap, -num)
            elif -num > heap[0]:
                heapq.heappop(heap)
                heapq.heappush(heap, -num)

        return [-x for x in heap]


# class Solution:
#     def getLeastNumbers(self, arr, k):
#         """
#         Args:
#             arr: list[int]
#             k: int
#         Return:
#             list[int]
#         """
#         if not arr or k == 0:
#             return []
#         self.arr = arr
#         # 最后一个参数表示要找的是下标为k - 1的数
#         return self.quick_search(0, len(arr) - 1, k - 1)

#     def quick_search(self, lo, hi, k):
#         """
#         Args: 
#             lo: int
#             hi: int
#             k: int
#         Return:
#             list[int]
#         """
#         # 每快排切分一次, 找到排序后小标为j的元素, 如果j恰好等于k就返回j以及j左边所有数
#         j = self.partition(lo, hi)
#         if j == k:
#             return self.arr[: j + 1]
#         # 否则根据下表j和k的大小关系来决定继续切分左段还是右段
#         elif j > k:
#             return self.quick_search(lo, j - 1, k)
#         else:
#             return self.quick_search(j + 1, hi, k)
    
#     def partition(self, lo, hi):
#         v = self.arr[lo]
#         i = lo
#         j = hi + 1
#         while True:
#             while i + 1 <= hi and self.arr[i + 1] < v:
#                 i += 1
#             i += 1
#             while j - 1 >= lo and self.arr[j - 1] > v:
#                 j -= 1
#             j -= 1
#             if i >= j:
#                 break
#             self.arr[i], self.arr[j] = self.arr[j], self.arr[i]
#         self.arr[lo] = self.arr[j]
#         self.arr[j] = v
#         return j


if __name__ == "__main__":
    arr = [3,2,1]
    k = 2
    print(Solution().getLeastNumbers(arr, k))