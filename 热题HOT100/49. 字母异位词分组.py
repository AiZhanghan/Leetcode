from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """Hash"""
        dic = {}
        for s in strs:
            key = [0 for _ in range(26)]
            for c in s:
                key[ord(c) - ord("a")] += 1
            key = (str(x) for x in key)
            key = "".join(key)
            if key in dic:
                dic[key].append(s)
            else:
                dic[key] = [s]
        return list(dic.values())


# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#         """排序 + Hash"""
#         dic = {}
#         for s in strs:
#             key = "".join(sorted(s))
#             if key in dic:
#                 dic[key].append(s)
#             else:
#                 dic[key] = [s]
#         return list(dic.values())


# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#         """HashMap"""
#         res = []
#         used = [False for _ in range(len(strs))]
#         for i in range(len(strs)):
#             if used[i]:
#                 continue
#             temp = []
#             temp.append(strs[i])
#             for j in range(i + 1, len(strs)):
#                 if not used[j] and self.equals(strs[i], strs[j]):
#                     used[j] = True
#                     temp.append(strs[j])
#             res.append(temp)
#         return res
    
#     def equals(self, s1: str, s2: str) -> bool:
#         dic = {}
#         for c in s1:
#             if c in dic:
#                 dic[c] += 1
#             else:
#                 dic[c] = 1
#         for c in s2:
#             if c in dic and dic[c] > 0:
#                 dic[c] -= 1
#             else:
#                 return False
#         for value in dic.values():
#             if value != 0:
#                 return False
#         return True
