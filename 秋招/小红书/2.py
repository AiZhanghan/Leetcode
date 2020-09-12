#******************************开始写代码******************************


def solution(s):
    """
    Args:
        s: str
    
    Return:
        int
    """
    if not s:
        return 0
    
    dp = [0 for _ in range(len(s) + 1)]
    # dp[0] = 1
    dic = {}
    for i in range(len(s)):
        if s[i] not in dic:
            dp[i + 1] = dp[i] + 1
            dic[s[i]] = i
        else:
            dp[i + 1] = min(dp[i], dp[dic[s[i]]]) + 1
    return dp[-1]


#******************************结束写代码******************************


try:
    _s = input()
except:
    _s = None

_s = "abaccd"  
res = solution(_s)

print(str(res) + "\n")