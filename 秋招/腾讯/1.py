class Solution:
    def func(self, nums1, nums2):
        """
        Args:
            nums1: list[int]
            nums2: list[int]
        
        Return:
            list[int]
        """
        nums1_set = set(nums1)
        nums2_set = set(nums2)
        res_set = nums1_set.intersection(nums2_set)
        res = list(res_set)
        res.sort(reverse=True)
        return res


if __name__ == "__main__":
    n = int(input()) 
    nums1 = list(map(int, input().split()))
    m = int(input()) 
    nums2 = list(map(int, input().split()))
    res = Solution().func(nums1, nums2)
    print(res)