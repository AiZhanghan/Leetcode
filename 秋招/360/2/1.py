class Solution:
    def func(self, s):
        """
        Args:
            s: str
        """
        s_splited = s.split("n")
        if s_splited[0]:
            print(s_splited[0].title())

        for i in range(1, len(s_splited)):
            s_splited[i] = "N" + s_splited[i]
            print(s_splited[i])


# class Solution:
#     def func(self, s):
#         """
#         Args:
#             s: str
#         """
#         s_splited = s.split("n")
#         for i in range(1, len(s_splited)):
#             s_splited[i] = "N" + s_splited[i]
        
#         if s_splited[0]:
#             print(s_splited[0].title())
        
#         for i in range(1, len(s_splited)):
#             print(s_splited[i])


if __name__ == "__main__":
    s = input()
    Solution().func(s)