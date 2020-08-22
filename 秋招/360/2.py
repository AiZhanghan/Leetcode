from collections import deque


class Solution:
    def func(self, nums, ops):
        """
        Args:
            nums: list[int]
            ops: list[int]
        
        Return:
            deque
        """
        nums = deque(nums)
        # 简化ops
        temp = []
        i = 0
        while i < len(ops) - 1:
            if ops[i] == 1:
                temp.append(1)
                i += 1
            else:
                if ops[i] == ops[i + 1]:
                    i += 2
                else:
                    temp.append(2)
                    i += 1
        temp.append(ops[-1])

        ops = temp
        for op in ops:
            if op == 1:
                self.op1(nums)
            else:
                self.op2(nums)
        return nums
    
    def op1(self, nums):
        """把排列的第1个数移到末尾

        Args:
            nums: deque
        """
        temp = nums.popleft()
        nums.append(temp)
    
    def op2(self, nums):
        """交换排列的第1个数与第2个数、第3个数与第4个数...第N-1个数与第N个数

        Args:
            nums: list[int] 
        """
        for i in range(0, len(nums), 2):
            nums[i], nums[i + 1] = nums[i + 1], nums[i]


if __name__ == "__main__":
    N, M = list(map(int, input().split()))
    nums = [x for x in range(1, N + 1)]
    ops = list(map(int, input().split()))
    res = Solution().func(nums, ops)
    print(" ".join(map(str, res)))