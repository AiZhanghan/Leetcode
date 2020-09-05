#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
# 
# @param nums int整型一维数组 整数数组 nums
# @param target int整型 目标值 target
# @return int整型一维数组
#
class Solution:
    def twoSum(self , nums , target ):
        # 时间复杂度 O(N)
        # 空间复杂度 O(N)
        # write code here
        # dic保存遍历过的数值与下标
        dic = {}
        for i, num in enumerate(nums):
            if target - num in dic:
                return [dic[target - num], i]
            dic[num] = i