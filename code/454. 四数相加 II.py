class Solution:
    def fourSumCount(self, A, B, C, D):
        """
        Args:
            A: list[int]
            B: list[int]
            C: list[int]
            D: list[int]
        
        Return:
            int
        """
        res = 0

        dic = {}
        for a in A:
            for b in B:
                a_b = a + b
                dic[a_b] = dic.get(a_b, 0) + 1
        
        for c in C:
            for d in D:
                target = -(c + d)
                if target in dic:
                    res += dic[target]
        return res