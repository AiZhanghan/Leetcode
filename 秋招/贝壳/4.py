class Solution:
    def func(self, nums, k, d):
        """
        Args:
            nums: list[list[int]]
            k: int
            d: int
        
        Return:
            int
        """
        row_sum = [sum(x) for x in nums]
        col_sum = [0 for _ in range(len(nums[0]))]
        for j in range(len(nums[0])):
            for i in range(len(nums)):
                col_sum[j] += nums[i][j]
        
        res = 0
        for _ in range(k):
            max_row_sum = max(row_sum)
            max_col_sum = max(col_sum)
            if max_row_sum >= max_col_sum:
                res += max_row_sum
                for i in range(len(row_sum)):
                    if row_sum[i] == max_row_sum:
                        break
                row_sum[i] -= len(col_sum) * d
                for i in range(len(col_sum)):
                    col_sum[i] -= d
            else:
                res += max_col_sum
                for i in range(len(col_sum)):
                    if col_sum[i] == max_col_sum:
                        break
                col_sum[i] -= len(row_sum) * d
                for i in range(len(row_sum)):
                    row_sum[i] -= d
        return res


if __name__ == "__main__":
    n, m, k, d = list(map(int, input().split()))
    nums = []
    for _ in range(n):
        nums.append(list(map(int, input().split())))
    # n, m, k, d = 2, 2, 2, 2
    # nums = [[2, 3], [3, 3]]
    print(Solution().func(nums, k, d))