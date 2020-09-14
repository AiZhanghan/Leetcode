class Solution:
    def func(self, money):
        """回溯

        Args:
            money: list[int]
        
        Return:
            int
        """
        if len(money) <= 5:
            return sum(money)
        
        self.res = 0
        self.dfs(money, 0, len(money) - 1, 0)
        
        return self.res
    
    def dfs(self, money, left, right, path):
        """
        Args:
            money: list[int]
            left: int
            right: int
            path: int
        """
        if left + len(money) - 1 - right == 5:
            self.res = max(self.res, path)
            return
        
        self.dfs(money, left + 1, right, path + money[left])
        self.dfs(money, left, right - 1, path + money[right])


if __name__ == "__main__":
    money = input()[1: -1].split(",")
    # money = "[]"
    # if money:
    try:
        money = list(map(int, money))
        # print(money)
        print(Solution().func(money))
    except:
        print(0)
    