class Solution:
    def productExceptSelf(self, nums):
        """
        Args:
            nums: list[int]
        
        Return:
            list[int]
        """
        answer = [0 for _ in range(len(nums))]
        
        answer[0] = 1
        for i in range(1, len(answer)):
            answer[i] = answer[i - 1] * nums[i - 1]
        
        r = 1
        for i in reversed(range(len(answer))):
            answer[i] = answer[i] * r
            r *= nums[i]
        
        return answer


# class Solution:
#     def productExceptSelf(self, nums):
#         """
#         Args:
#             nums: list[int]
        
#         Return:
#             list[int]
#         """
#         length = len(nums)

#         L = [0 for _ in range(length)]
#         R = [0 for _ in range(length)]
#         answer = [0 for _ in range(length)]

#         L[0] = 1
#         for i in range(1, length):
#             L[i] = L[i - 1] * nums[i - 1]

#         R[-1] = 1
#         for i in range(length - 2, -1, -1):
#             R[i] = R[i + 1] * nums[i + 1]

#         for i in range(length):
#             answer[i] = L[i] * R[i]
        
#         return answer