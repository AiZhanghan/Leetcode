class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        start = 0
        end = 0
        for i in range(len(s)):
            len1 = self.expand_around_center(s, i, i)
            len2 = self.expand_around_center(s, i, i + 1)
            len_ = max(len1, len2)
            if len_ > end - start + 1:
                start = i - (len_ - 1) // 2
                end = i + len_ // 2
        return s[start: end + 1]

    def expand_around_center(self, s: str, left: int, right: int) -> int:
        l = left
        r = right
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return r - l - 1


if __name__ == "__main__":
    s = "babad"
    print(Solution().longestPalindrome(s))