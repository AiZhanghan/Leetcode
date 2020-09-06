class Solution:
    def func(self, a, b):
        """
        Args:
            a: list[int]
            b: list[int]
        
        Return:
            list[int]
        """
        a_set = set(a)
        b_set = set(b)
        res = [
            len(a_set - b_set), 
            len(b_set - a_set), 
            len(a_set.intersection(b_set))
        ]
        return res
        

if __name__ == "__main__":
    n, p, q = list(map(int, input().split()))
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    res = Solution().func(a, b)
    for x in res:
        print(x, end=" ")