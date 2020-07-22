import collections


class Solution:
    def parallelogram(self, nums):
        """
        Args:
            nums: list[int]
        
        Return:
            int
        """
        counter = collections.Counter(nums)
        max1 = 0
        max2 = 0
        for key, value in counter.items():
            if value < 2:
                continue
            elif value < 4:
                if key > max1:
                    max2 = max1
                    max1 = key
                elif key > max2:
                    max2 = key
            else:
                if key > max1:
                    max2 = key
                    max1 = key
                if key > max2:
                    max2 = key
        
        area = max1 * max2
        return area if area != 0 else -1


if __name__ == "__main__":
    n = int(input())
    nums = list(map(int, input().split()))
    # n = 5
    # nums = [2, 2, 4, 4, 4, 4, 5]
    print(Solution().parallelogram(nums))
