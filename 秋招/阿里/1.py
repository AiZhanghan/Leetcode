class Solution:
    def func(self, S, T):
        """
        Args:
            S: str
            T: str
        
        Return:
            int
        """
        self.memo = {}
        res = 0
        l = 0
        r = 0
        while r < len(S):
            while not self.helper(S[l: r + 1], T):
                l += 1
            res += r - l + 1
            r += 1
        return res

    def helper(self, sub_str, T):
        """
        sub_str是不是T的子序列

        Args:
            sub_str: str
            T: str
        
        Return:
            bool
        """
        if not sub_str:
            return True
        if sub_str in self.memo:
            return self.memo[sub_str]
        res = True
        i = 0
        for c in sub_str:
            while i < len(T):
                if T[i] == c:
                    break
                i += 1
            if i == len(T):
                res = False
            i += 1
        self.memo[sub_str] = res
        return res


if __name__ == "__main__":
    # n, m = list(map(int, input().split()))
    # S = input()
    # T = input()
    S = "beihang" # "zhanhan"
    T = "huangzhenkai"
    print(Solution().func(S, T))