class Solution:
    def maxSubArray(self, nums):
        """
        parameter:
            nums: list[int]
        return: int
        """
        temp = nums[0]
        max_ = temp
        for i in range(1, len(nums)):
            if temp > 0:
                temp += nums[i]
                max_ = max(temp, max_)
            else:
                temp = nums[i]
                max_ = max(temp, max_)
        return max_
        

# class Solution:
#     def maxSubArray(self, nums):
#         """
#         parameter:
#             nums: list[int]
#         return: int
#         """
#         if not nums:
#             return 0

#         self.nums = nums
#         return self.divide_and_conquer(0, len(nums)-1)

#     def divide_and_conquer(self, left, right):
#         """
#         parameter:
#             left: int
#             right: int
#         return: int
#         """
#         if left == right:
#             return self.nums[left]
        
#         mid = (left + right) // 2
#         left_max_sum = self.divide_and_conquer(left, mid)
#         right_max_sum = self.divide_and_conquer(mid+1, right) 
        
#         left_board_sum = self.nums[mid]
#         right_board_sum = self.nums[mid+1]
#         max_left_board_sum = self.nums[mid]
#         max_right_board_sum = self.nums[mid+1]
#         # 向左扫描
#         for i in range(mid-1, -1, -1):
#             left_board_sum += self.nums[i]
#             if left_board_sum > max_left_board_sum:
#                 max_left_board_sum = left_board_sum
#         # 向右扫描
#         for i in range(mid+2, right+1):
#             right_board_sum += self.nums[i]
#             if right_board_sum > max_right_board_sum:
#                 max_right_board_sum = right_board_sum

#         return max(left_max_sum, right_max_sum, max_left_board_sum+max_right_board_sum)
