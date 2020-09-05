#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
# 返回能交换奖品的最大数量
# @param a int整型 
# @param b int整型 
# @param c int整型 
# @return int整型
#
class Solution:
    def numberofprize(self , a , b , c ):
        # write code here
        nums = [a, b, c]
        return self.helper(nums)
    
    def helper(self, nums):
        nums.sort()
        if nums[0] == 0 and nums[1] == 0:
            if nums[2] < 5:
                return 0
            temp = nums[2] * 2 // 5
            return self.helper([temp, temp, nums[2] - 4 * temp])
        if nums[0] == 0:
            temp = nums[2] * 2 // 3
            if temp > nums[1]:
                temp = nums[1]
            return self.helper([temp, nums[1], nums[2] - temp * 2])
        
        res = nums[0]
        res += self.helper([0, nums[1] - nums[0], nums[2] - nums[0]])
        
        return res


if __name__ == "__main__":
    a, b, c = [2, 4, 4]
    print(Solution().numberofprize(a, b, c))