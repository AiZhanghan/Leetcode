class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        res = 0
        dic = {}
        for r, char in enumerate(s):
            if char in dic:
                l = max(l, dic[char])
            res = max(res, r - l + 1)
            dic[char] = r + 1
        return res


# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         l = 0
#         r = 0
#         res = 0
#         for char in s:
#             if char in s[l: r]:
#                 l = s.index(char, l, r) + 1
#             r += 1
#             res = max(res, r - l)
#         return res        
