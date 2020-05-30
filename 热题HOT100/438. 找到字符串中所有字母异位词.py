class Solution:
    def findAnagrams(self, s, p):
        """
        Args；
            s: str
            p: str
        
        Return:
            list[int]
        """
        need = {}
        window = {}
        for c in p:
            need[c] = need.get(c, 0) + 1
        
        left = 0
        right = 0
        valid = 0
        res = []

        while right < len(s):
            c = s[right]
            right += 1
            if c in need:
                window[c] = window.get(c, 0) + 1
                if window[c] == need[c]:
                    valid += 1

            while right - left >= len(p):
                if valid == len(need):
                    res.append(left)
                d = s[left]
                left += 1
                if d in need:
                    if window[d] == need[d]:
                        valid -= 1
                    window[d] -= 1
        return res


# from collections import Counter


# class Solution:
#     def findAnagrams(self, s, p):
#         """
#         Args；
#             s: str
#             p: str
        
#         Return:
#             list[int]
#         """
#         if len(s) < len(p):
#             return []

#         res = []
#         left = 0
#         right = len(p) - 1

#         counter = Counter(p)

#         for i in range(right + 1):
#             if s[i] in counter:
#                 counter[s[i]] -= 1
#         if self.is_zeros(counter):
#             res.append(0)

#         for right in range(len(p), len(s)):
#             if s[right] in counter:
#                 counter[s[right]] -= 1
#             left = right - len(p) + 1
#             if s[left - 1] in counter:
#                 counter[s[left - 1]] += 1
#             if self.is_zeros(counter):
#                 res.append(left)
        
#         return res

#     def is_zeros(self, counter):
#         """
#         Args:
#             counter: Counter
        
#         Return:
#             bool
#         """
#         for value in counter.values():
#             if value != 0:
#                 return False
#         return True


# class Solution:
#     def findAnagrams(self, s, p):
#         """
#         Args；
#             s: str
#             p: str
        
#         Return:
#             list[int]
#         """
#         res = []
#         left = 0
#         right = len(p)
#         p = sorted(p)
#         while right <= len(s):
#             if sorted(s[left: right]) == p:
#                 res.append(left)
#             left += 1
#             right += 1
#         return res