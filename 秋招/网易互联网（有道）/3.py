class Solution:
    def earlest_off_time(self, a, b):
        """
        Args:
            a: list[int]
            b: list[int]
        
        Return:
            str
        """
        if not b:
            need_seconds = a[0]  
        else:
            need_seconds = self.least_need_second(a, b)
        hours = need_seconds // 3600
        mins = (need_seconds - hours * 3600) // 60
        seconds = need_seconds % 60
        
        if hours + 8 >= 12:
            end = "pm"
            hours = hours + 8 - 12
            hours_str = ("0" if hours < 10 else "") + str(hours)
        else:
            end = "am"
            hours = hours + 8
            hours_str = ("0" if hours < 10 else "") + str(hours)
        # hours_str = ("0" if (hours + 8) < 10 else "") + str(hours + 8) 
        mins_str = ("0" if mins < 10 else "") + str(mins)
        seconds_str = ("0" if seconds < 10 else "") + str(seconds)

        res = "%s:%s:%s " % (hours_str, mins_str, seconds_str)
        # if hours + 8 >= 12:
        #     res = str(hours - 12) + res[2:]
        #     res += "pm"
        # else:
        #     res += "am"
        
        return res + end

    def least_need_second(self, a, b):
        """
        Args:
            a: list[int]
            b: list[int]
        
        Return:
            int
        """
        # dp[0][i], i客户和i - 1分开买所需最少时间
        # dp[1][i], i客户和i - 1一起买所需最少时间
        dp = [[0 for _ in range(len(b))] for _ in range(2)]
        dp[0][0] = a[0] + a[1]
        dp[1][0] = b[0]

        for i in range(1, len(dp[0])):
            dp[0][i] = min(dp[0][i - 1], dp[1][i - 1]) + a[i + 1]
            dp[1][i] = dp[0][i - 1] - a[i] + b[i]
        
        return min(dp[0][-1], dp[1][-1])


if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        n = int(input())
        a = list(map(int, input().split()))
        # b = None
        # if n > 1:
        b = list(map(int, input().split()))
        print(Solution().earlest_off_time(a, b))
        