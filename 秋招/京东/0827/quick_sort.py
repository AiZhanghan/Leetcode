class Solution:
    def quick_sort(self, items):
        """
        Args
            items: list[int]
        """
        self._quick_sort(items, 0, len(items) - 1)
    
    def _quick_sort(self, items, start, end):
        """
        Args:
            items: list[int]
            start: int
            end: int
        """
        if start >= end:
            return
        pivot_index = self.partition(items, start, end)
        
        self._quick_sort(items, start, pivot_index - 1)
        self._quick_sort(items, pivot_index + 1, end)
    
    def partition(self, items, start, end):
        """
        Args:
            items: list[int]
            start: int
            end: int
        
        Return:
            int
        """
        # [0, i) >= pivot
        i = start
        pivot = items[end]
        for j in range(start, end):
            if items[j] >= pivot:
                items[i], items[j] = items[j], items[i]
                i += 1
        items[i], items[end] = items[end], items[i]
        return i


if __name__ == "__main__":
    items = [2, 4, 10, 34, 1, 0]
    Solution().quick_sort(items)
    print(items)