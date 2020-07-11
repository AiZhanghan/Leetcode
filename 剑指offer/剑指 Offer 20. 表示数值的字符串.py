class Solution:
    def isNumber(self, s):
        """
        Args:
            s: str
        
        Return:
            bool
        """
        num_seen = False
        dot_seen = False
        e_seen = False
        s = s.strip()
        for i in range(len(s)):
            if s[i].isdigit():
                num_seen = True
            elif s[i] == ".":
                if dot_seen or e_seen:
                    return False
                dot_seen = True
            elif s[i] == "e" or s[i] == "E":
                if e_seen or not num_seen:
                    return False
                e_seen = True
                num_seen = False
            elif s[i] == "-" or s[i] == "+":
                if i != 0 and s[i - 1] != "e" and s[i - 1] != "E":
                    return False
            else:
                return False
        return num_seen