class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        #[i, j)内为重复元素
        i = 0
        #被删除元素个数:j - i - 1
        remove_num= 0
        #数组长度
        lenth = len(nums)
        while i + 1 < len(nums) - remove_num:
            
            j = i + 1
            while nums[j] == nums[i]:
                j += 1
            
            if j - i <= 2:
                i = j
                continue
            else:
                remove_num += j - i - 2
                