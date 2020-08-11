class Solution:
    def func(self, s):
        """
        Args:
            s: str
        
        Return:
            int
        """
        if len(s) % 2 == 0:
            right = len(s) // 2
            left = right - 1
        else:
            right = len(s) // 2 + 1
            left = len(s) // 2 - 1
        
        count = 0
        while left >= 0 and right < len(s):
            if s[left] != s[right]:
                count += 1
            left -= 1
            right += 1
        
        return count
    

if __name__ == "__main__":
    N = int(input())
    s = input()
    print(Solution().func(s))