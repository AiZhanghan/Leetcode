class Solution:
    def nextGreaterElements(self, nums):
        """
        Args:
            nums: list[int]
        
        Return:
            list[int]
        """
        res = [-1 for _ in range(len(nums))]
        stack = []
        for _ in range(2):
            for i in range(len(nums)):
                while stack and nums[i] > nums[stack[-1]]:
                    j = stack.pop()
                    if res[j] == -1:
                        res[j] = nums[i]
                stack.append(i)
        return res