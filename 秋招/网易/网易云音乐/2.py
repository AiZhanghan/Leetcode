from collections import defaultdict

class Solution:
    def func(self, nums, T, K):
        """
        Args:
            nums: list[int]
            T: int
            K: int
        
        Return:
            int
        """
        res = 0
        dic = defaultdict(list)
        
        for i, num in enumerate(nums):
            other = T - num
            if other in dic:
                for j in dic[other]:
                    if i - j <= K:
                        res += 1
            dic[num].append(i)
        
        return res


if __name__ == "__main__":
    T, K = list(map(int, input().split()))
    nums = list(map(int, input().split()))
    print(Solution().func(nums, T, K))
    