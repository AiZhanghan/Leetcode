class Solution:
    def matrixReshape(self, nums, r, c):
        """
        Args:
            nums: list[list[int]]
            r: int
            c: int
        
        Return:
            list[list[int]]
        """
        m = len(nums)
        n = len(nums[0])
        if m * n != r * c:
            return nums
        res = []
        count = 0
        temp = []
        for i in range(m):
            for j in range(n):
                temp.append(nums[i][j])
                count += 1
                if count == c:
                    res.append(temp[:])
                    temp = []
                    count = 0
        return res