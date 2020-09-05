#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
# 返回能创建的房屋数
# @param t int整型 要建的房屋面宽
# @param xa int整型一维数组 已有房屋的值，其中 x0 a0 x1 a1 x2 a2 ... xi ai 就是所有房屋的坐标和房屋面宽。 其中坐标是有序的（由小到大）
# @return int整型
#
class Solution:
    def getHouses(self , t , xa ):
        # write code here
        if not xa:
            return 0
        res = 2
        # 边界
        boards = []
        for i in range(0, len(xa), 2):
            boards.append([xa[i] - xa[i + 1] / 2, xa[i] + xa[i + 1] / 2])
        
        for i in range(len(boards) - 1):
            if boards[i + 1][0] - boards[i][1] > t:
                res += 2
            elif boards[i + 1][0] - boards[i][1] == t:
                res += 1
        return res


if __name__ == "__main__":
    t = 2
    xa = [-1, 4, 5, 2]
    print(Solution().getHouses(t, xa))