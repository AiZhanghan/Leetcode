class Solution:
    def findShortestSubArray(self, nums):
        """
        Args:
            nums: list[int]
        
        Return:
            int
        """
        dic = {}
        for i, num in enumerate(nums):
            if num not in dic:
                dic[num] = [i, i, 1]
            else:
                dic[num][1] = i
                dic[num][2] += 1
        
        max_freq = 0
        res = float("inf")
        for key in dic:
            start, end, freq = dic[key]
            if freq == max_freq:
                res = min(res, end - start + 1)
            elif freq > max_freq:
                max_freq = freq
                res = end - start + 1
        return res


if __name__ == "__main__":
    nums = [1,2,2,3,1,4,2]
    print(Solution().findShortestSubArray(nums))