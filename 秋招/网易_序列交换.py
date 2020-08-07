class Solution:
    def sequence_exchange(self, nums):
        """
        Args:
            nums: list[int]
        
        Return:
            list[int]
        """
        has_odd = False
        has_even = False
        for num in nums:
            if num % 2:
                has_odd = True
            else:
                has_even = True
            if has_odd and has_even:
                return sorted(nums)
        return nums
    

if __name__ == "__main__":
    n = int(input())
    nums = list(map(int, input().split()))
    s = Solution()
    res = s.sequence_exchange(nums)
    for x in res:
        print(x, end=" ")
            