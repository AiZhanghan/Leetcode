import collections


class Solution:
    def frequencySort(self, s):
        """
        Args:
            s: str
        
        Return:
            str
        """
        counter = collections.Counter(s)
        counter_list = list(counter.items())
        counter_list.sort(key=lambda x: x[1], reverse=True)
        res = []
        for c, time in counter_list:
            res.extend([c] * time)
        return "".join(res)