class Solution:
    def findUnsortedSubarray(self, nums):
        """O(n)

        Args:
            nums: list[int]
        
        Return: 
            int
        """
        _min = float("inf")
        _max = -float("inf")
        flag = False
        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1]:
                flag = True
            if flag:
                _min = min(_min, nums[i])
        flag = False
        for i in reversed(range(len(nums) - 1)):
            if nums[i] > nums[i + 1]:
                flag = True
            if flag:
                _max = max(_max, nums[i])
        for l in range(len(nums)):
            if nums[l] > _min:
                break
        for r in reversed(range(len(nums))):
            if nums[r] < _max:
                break
        return r - l + 1 if r > l else 0


# class Solution:
#     def findUnsortedSubarray(self, nums):
#         """栈 O(n)

#         Args:
#             nums: list[int]
        
#         Return: 
#             int
#         """
#         l = len(nums) - 1
#         r = 0
#         stack = []
#         for i in range(len(nums)):
#             while stack and nums[stack[-1]] > nums[i]:
#                 l = min(l, stack.pop())
#             stack.append(i)
#         stack = []
#         for i in reversed(range(len(nums))):
#             while stack and nums[stack[-1]] < nums[i]:
#                 r = max(r, stack.pop())
#             stack.append(i)
#         return r - l + 1 if r > l else 0


# class Solution:
#     def findUnsortedSubarray(self, nums):
#         """排序 O(nlog(n))

#         Args:
#             nums: list[int]
        
#         Return: 
#             int
#         """
#         start = len(nums) - 1
#         end = 0
#         sorted_nums = sorted(nums)
#         for i in range(len(nums)):
#             if nums[i] != sorted_nums[i]:
#                 start = min(start, i)
#                 end = max(start, i)
#         return end - start + 1 if end > start else 0



# class Solution:
#     def findUnsortedSubarray(self, nums):
#         """暴力O(n ^ 2)

#         Args:
#             nums: list[int]
        
#         Return: 
#             int
#         """
#         l = len(nums) - 1
#         r = 0
#         for i in range(len(nums)):
#             for j in range(i + 1, len(nums)):
#                 if nums[j] < nums[i]:
#                     l = min(l, i)
#                     r = max(r, j)
#         return r - l + 1 if r - l > 0 else 0


# class Solution:
#     def findUnsortedSubarray(self, nums):
#         """暴力O(n ^ 3)

#         Args:
#             nums: list[int]
        
#         Return: 
#             int
#         """
#         res = len(nums)
#         for i in range(len(nums)):
#             for j in range(i, len(nums) + 1):
#                 _min = float("inf")
#                 _max = -float("inf")
#                 prev = -float("inf")
#                 for k in range(i, j):
#                     _min = min(_min, nums[k])
#                     _max = max(_max, nums[k])
#                 if i > 0 and nums[i - 1] > _min or \
#                     j < len(nums) and nums[j] < _max:
#                     continue
#                 k = 0
#                 while k < i and prev <= nums[k]:
#                     prev = nums[k]
#                     k += 1
#                 if k != i:
#                     continue
#                 k = j
#                 while k < len(nums) and prev <= nums[k]:
#                     prev = nums[k]
#                     k += 1
#                 if k == len(nums):
#                     res = min(res, j - i)
#         return res


if __name__ == "__main__":
    nums = [2,6,4,8,10,9,15]
    print(Solution().findUnsortedSubarray(nums))