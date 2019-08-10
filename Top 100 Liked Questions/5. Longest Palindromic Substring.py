# -*- coding: utf-8 -*-
"""
Created on Sat Aug 10 16:25:41 2019

@author: 54949
"""

class Solution:
    def longestPalindrome(self, s: str) -> str:
        '''
        递归 + 记忆化搜索
        '''
        # [l....r)
        l = 0
        r = len(s)
        # list, 最长回文子串左右索引
        res = [0, 1]
        self.memo = [[None for _ in range(r + 1)] for _ in range(r + 1)]
        
        res = self.longest_palindrome(s, l, r, res)
        
        return s[res[0]: res[1]]
    
    def longest_palindrome(self, s, l, r, res):
        # 剪枝
        if r - l <= res[1] - res[0]:
            return res
        
        if self.is_palindrome(s[l: r]):
            res[0] = l
            res[1] = r
            return res
        
        if self.memo[l][r]:
            return self.memo[l][r]
        
        left_res = self.longest_palindrome(s, l, r - 1, res)
        right_res = self.longest_palindrome(s, l + 1, r, res)
        
        if right_res[1] - right_res[0] > left_res[1] - left_res[0]:
            res = right_res
        else:
            res = left_res
        
        self.memo[l][r] = res
        
        return res
            
    def is_palindrome(self, s):
        
        l = 0
        r = len(s) - 1
        
        while l <= r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        
        return True

if __name__ == '__main__':
    s = "lphbehiapswjudnbcossedgioawodnwdruaaxhbkwrxyzaxygmnjgwysafuqbmtzwdkihbwkrjefrsgjbrycembzzlwhxneiijgzidhngbmxwkhphoctpilgooitqbpjxhwrekiqupmlcvawaiposqttsdgzcsjqrmlgyvkkipfigttahljdhtksrozehkzgshekeaxezrswvtinyouomqybqsrtegwwqhqivgnyehpzrhgzckpnnpvajqevbzeksvbezoqygjtdouecnhpjibmsgmcqcgxwzlzztdneahixxhwwuehfsiqghgeunpxgvavqbqrelnvhnnyqnjqfysfltclzeoaletjfzskzvcdwhlbmwbdkxnyqappjzwlowslwcbbmcxoiqkjaqqwvkybimebapkorhfdzntodhpbhgmsspgkbetmgkqlolsltpulgsmyapgjeswazvhxedqsypejwuzlvegtusjcsoenrcmypexkjxyduohlvkhwbrtzjnarusbouwamazzejhnetfqbidalfomecehfmzqkhndpkxinzkpxvhwargbwvaeqbzdhxzmmeeozxxtzpylohvdwoqocvutcelgdsnmubyeeeufdaoznxpvdiwnkjliqtgcmvhilndcdelpnilszzerdcuokyhcxjuedjielvngarsgxkemvhlzuprywlypxeezaxoqfges"
    res = Solution().longestPalindrome(s)