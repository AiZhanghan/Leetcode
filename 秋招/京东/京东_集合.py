# class Solution:
#     def merge(self, A, B):
#         """
#         Args:
#             A: list[int]
#             B: list[int]
        
#         Return:
#             list[int]
#         """
#         A.sort()
#         B.sort()
class Solution:
    def merge(self, A, B):
        """
        Args:
            A: list[int]
            B: list[int]
        
        Return:
            list[int]
        """
        A += B
        return " ".join(map(str, sorted(set(A))))


#         i = 0
#         j = 0
#         res = []
#         while i < len(A) and j < len(B):
#             if A[i] < B[j]:
#                 res.append(A[i])
#                 i += 1
#             elif A[i] > B[j]:
#                 res.append(B[j])
#                 j += 1
#             else:
#                 res.append(A[i])
#                 i += 1
#                 j += 1
#         while i < len(A):
#             res.append(A[i])
#             i += 1
#         while j < len(B):
#             res.append(B[j])
#             j += 1
#         return " ".join(map(str, res))


def main():

    while True:
        n, m = list(map(int, input().split()))
        A = list(map(int, input().split()))
        B = list(map(int, input().split()))
        print(Solution().merge(A, B))


if __name__ == "__main__":
    main()
