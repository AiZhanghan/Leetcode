class Solution:
    def removeDuplicates(self, nums) -> int:
        #[i, j)内为重复元素
        i = 0
        #被删除元素个数:j - i - 1
        remove_num= 0
        #数组长度
        lenth = len(nums)
        while i + 2 < len(nums) - remove_num:
            
            j = i + 1
            while j < len(nums) - remove_num and nums[j] == nums[i]:
                j += 1
            
            #没有重复
            if j - i <= 2:
                i = j
                continue
            else:
                redundance_num = j - i - 2
                nums[i + 2: lenth - remove_num - redundance_num] = nums[j: lenth - remove_num]
                remove_num += redundance_num
                i += 2
        
        return lenth - remove_num
    
if __name__ == '__main__':
    arr = [0,1,2,2,2,2,2,3,4,4,4]
    
    res = Solution().removeDuplicates(nums=arr)
    
    print(arr, res)