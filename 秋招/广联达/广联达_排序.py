class Solution:
    def my_sort(self, nums):
        """
        Args:
            nums: list[int]
        
        Return:
            int
        """
        stack = [nums[0]]
        # 不能加入非严格递增单调栈的元素数目
        count = 0
        # 栈中比非栈中元素大的元素下标
        index = 0
        for num in nums[1:]:
            if stack[-1] <= num:
                stack.append(num)
            else:
                count += 1
                while num > stack[index]:
                    index += 1
        return index + count


if __name__ == "__main__":
    n = int(input())
    nums = list(map(int, input().split()))
    # n = 4
    # nums = [1, 6, 9 ,9, 5, 8, 0, 1, 12]
    print(Solution().my_sort(nums))
