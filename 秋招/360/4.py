from collections import deque


class Solution:
    def func(self, N, ops):
        """
        Args:
            N: int
            ops: list[int]
        
        Return:
            deque
        """
        odd = deque([x for x in range(1, N + 1, 2)])
        even = deque([x for x in range(2, N + 1, 2)])
        
        for op in ops:
            if op == 1:
                temp = odd.popleft()
                odd.append(temp) 
            odd, even = even, odd
        res = []
        for i in range(len(odd)):
            res.append(odd[i])
            res.append(even[i])
        return res


if __name__ == "__main__":
    # N, M = list(map(int, input().split()))
    # ops = list(map(int, input().split()))
    N = 2
    ops = [2]
    res = Solution().func(N, ops)
    print(" ".join(map(str, res)))