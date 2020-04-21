class Solution:
    def reverseWords(self, s):
        """
        Args:
            s: str
        
        Return:
            str
        """
        s = s.strip()
        res = []
        i = len(s) - 1
        j = len(s) - 1
        while i >= 0:
            # 搜索第一个空格
            while i >= 0 and s[i] != " ":
                i -= 1
            # 添加单词
            res.append(s[i + 1: j + 1])
            # 跳过单词间的空格
            while i >= 0 and s[i] == " ":
                i -= 1
            # j指向下一个单词的结尾
            j = i
        return " ".join(res)


# class Solution:
#     def reverseWords(self, s):
#         """
#         Args:
#             s: str
        
#         Return:
#             str
#         """
#         return " ".join(reversed(s.strip().split()))