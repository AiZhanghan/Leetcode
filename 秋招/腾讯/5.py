class Solution:
    def func(self, nums, colors):
        """
        Args:
            nums: list[int]
            colors: list[str]
        
        Return:
            int
        """
        red = []
        black = []
        for i in range(len(nums)):
            if colors[i] == "B":
                black.append((nums[i], i))
            else:
                red.append((nums[i], i))
        
        reverse_count = 0
        max_distance = -1
        for i in range(len(red)):
            for j in range(i):
                if red[i][0] < red[j][0]:
                    reverse_count += 1
                    max_distance = max(max_distance, red[i][1] - red[j][1])
        
        for i in range(len(black)):
            for j in range(i):
                if black[i][0] < black[j][0]:
                    reverse_count += 1
                    max_distance = max(max_distance, black[i][1] - black[j][1])
        
        return reverse_count + max_distance - 1


if __name__ == "__main__":
    n = int(input())
    colors = input()
    nums = list(map(int, input().split()))
    print(Solution().func(nums, colors))
