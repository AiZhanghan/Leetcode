class Solution:
    def aoe(self, nums, y):
        """
        Args:
            nums: list[list[int]]
                    [X, HP]
            y: int
            
        Return:
            int
        """
        res = 0
        nums.sort(key=lambda x: x[1], reverse=True)
        while nums:
            x1, hp1 = nums[0]
            res += hp1
            to_delete = [0]
            i = 1
            while i < len(nums) and abs(nums[i][0] - x1) > 2 * y:
                i += 1
            if i != len(nums):
                x2, _ = nums[i]
                to_delete.append(i)
                i += 1
                x = (x1 + x2) // 2
                while i < len(nums) and abs(x - nums[i][0]) <= 5:
                    to_delete.append(i)
                    i += 1
            for i, val in enumerate(to_delete):
                nums.pop(val - i)
        return res


if __name__ == "__main__":
    n, y = list(map(int, input().split()))
    nums = []
    for _ in range(n):
        nums.append(list(map(int, input().split())))

    print(Solution().aoe(nums, y))
