from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = -float("inf")
        imax = 1
        imin = 1
        for num in nums:
            if num < 0:
                imax, imin = imin, imax
            imax = max(imax * num, num)
            imin = min(imin * num, num)
            res = max(res, imax)
        return res