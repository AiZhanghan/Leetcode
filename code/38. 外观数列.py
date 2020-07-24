class Solution:
    def countAndSay(self, n):
        """
        Args:
            n: int
        
        Return:
            str
        """
        s = "1"
        for _ in range(1, n):
            temp = []
            count = 1
            for i in range(len(s) - 1):
                if s[i] == s[i + 1]:
                    count += 1
                else:
                    temp.append(str(count) + s[i])
                    count = 1
            temp.append(str(count) + s[-1])
            s = "".join(temp)
        return s