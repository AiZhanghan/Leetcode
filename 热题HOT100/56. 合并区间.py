from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        res = []
        for interval in intervals:
            if not res or interval[0] > res[-1][1]:
                res.append(interval)
            else:
                res[-1][1] = max(res[-1][1], interval[1])
        return res


# class Solution:
#     def merge(self, intervals: List[List[int]]) -> List[List[int]]:
#         intervals.sort(key=lambda x: x[0])
#         res = []
#         i = 0
#         while i < len(intervals):
#             temp = intervals[i]
#             while i + 1 < len(intervals) and temp[1] >= intervals[i + 1][0]:
#                 i += 1
#                 temp[1] = max(temp[1], intervals[i][1])
#             res.append(temp)
#             i += 1
#         return res