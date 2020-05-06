class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        Args:
            s: str
        
        Return:
            int
        """
        max_len = 0
        cur_len = 0
        dic = {}
        for i in range(len(s)):
            if s[i] not in dic or i - dic[s[i]] > cur_len:
                cur_len += 1
            else:
                cur_len = i - dic[s[i]]
            dic[s[i]] = i
            max_len = max(max_len, cur_len)
        return max_len


# class Solution:
#     def lengthOfLongestSubstring(self, s):
#         """
#         Args:
#             s: str
        
#         Return:
#             int
#         """
#         res = 0
#         l = 0
#         dic = {}
#         for r in range(len(s)):
#             if s[r] in dic:
#                 l = max(l, dic[s[r]])
#             dic[s[r]] = r + 1
#             res = max(res, r - l + 1)
#         return res


# class Solution:
#     def lengthOfLongestSubstring(self, s):
#         """
#         Args:
#             s: str
        
#         Return:
#             int
#         """
#         res = 0
#         l = 0
#         for r in range(len(s)):
#             for i in range(l, r):
#                 if s[r] == s[i]:
#                     l = i + 1
#                     break
#             res = max(res, r - l + 1)
#         return res


if __name__ == "__main__":
    s = "abba"
    print(Solution().lengthOfLongestSubstring(s))