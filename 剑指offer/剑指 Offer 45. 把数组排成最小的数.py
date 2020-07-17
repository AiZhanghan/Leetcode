class Solution:
    def minNumber(self, nums):
        """
        Args:
            nums: list[int]
        
        Return:
            str
        """
        self.strs = [str(num) for num in nums]
        self.quick_sort(0, len(self.strs) - 1)

        return "".join(self.strs)
    
    def quick_sort(self, lo, hi):
        """
        Args:
            lo: int
            hi: int
        """
        if lo >= hi:
            return
        j = self.partition(lo, hi)
        self.quick_sort(lo, j - 1)
        self.quick_sort(j + 1, hi)
    
    def partition(self, lo, hi):
        """
        Args:
            lo: int
            hi: int
        """
        i = lo
        j = hi + 1
        v = self.strs[lo]
        while True:
            while i + 1 <= hi and \
                self.strs[i + 1] + v < v + self.strs[i + 1]:
                i += 1
            i += 1
            while j - 1 >= lo and \
                self.strs[j - 1] + v > v + self.strs[j - 1]:
                j -= 1
            j -= 1
            if i >= j:
                break
            self.strs[i], self.strs[j] = self.strs[j], self.strs[i]
        self.strs[lo], self.strs[j] = self.strs[j], self.strs[lo]
        return j
