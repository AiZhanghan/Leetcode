class Solution:
    def func(self, nums1, nums2):
        """
        Args:
            nums1: list[int]
            nums2: list[int]
        
        Return:
            list[int]
        """
        p1 = 0
        p2 = 0
        res = []
        while p1 < len(nums1) and p2 < len(nums1):
            if nums1[p1] < nums2[p2]:
                p2 += 1
            elif nums1[p1] > nums2[p2]:
                p1 += 1
            else:
                res.append(nums1[p1])
                p1 += 1
                p2 += 1
        return res


if __name__ == "__main__":
    # nums1 = [23, 10, 9, 9, 6, 1]
    # num2 = [12, 9, 9, 7, 1, 1]
    n = int(input()) 
    nums1 = list(map(int, input().split()))
    m = int(input()) 
    nums2 = list(map(int, input().split()))
    res = Solution().func(nums1, nums2)
    # for x in res:
    #     print(x, end=" ")
    print(" ".join(map(str, res)))