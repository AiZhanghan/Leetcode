class Solution:
    def reverseVowels(self, s):
        """
        Args:
            s: str
        
        Return:
            str
        """
        vowels = set(["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"])
        s_list = list(s)
        l = 0
        r = len(s_list) - 1
        while l < r:
            if s_list[l] in vowels and s_list[r] in vowels:
                s_list[l], s_list[r] = s_list[r], s_list[l]
                l += 1
                r -= 1
            elif s_list[l] not in vowels:
                l += 1
            elif s_list[r] not in vowels:
                r -= 1
                
        return "".join(s_list)


if __name__ == "__main__":
    s = ".,"
    print(Solution().reverseVowels(s))