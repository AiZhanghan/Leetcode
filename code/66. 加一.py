class Solution:
    def plusOne(self, digits):
        """
        Args:
            digits: list[int]
        
        Return:
            list[int]
        """
        i = len(digits) - 1
        while i >= 0:
            if digits[i] == 9:
                digits[i] = 0
                i -= 1
            else:
                digits[i] += 1
                return digits
        digits.insert(0, 1)
        return digits