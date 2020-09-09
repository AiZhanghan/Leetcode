class Solution:
    def nextGreatestLetter(self, letters, target):
        """
        Args:
            letters: list[str]
            target: str
        
        Return:
            str
        """
        if not letters:
            return ""
        left = 0
        right = len(letters) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if letters[mid] < target:
                left = mid + 1
            elif letters[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return letters[left] if left < len(letters) else letters[0]


if __name__ == "__main__":
    letters = ["c", "f", "j"]
    target = "a"
    print(Solution().nextGreatestLetter(letters, target))