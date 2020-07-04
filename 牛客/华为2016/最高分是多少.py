class Solution:
    def __init__(self, values):
        """
        Args:
            values: list[int]
        """
        self.values = values
        
    def Q(self, A, B):
        """
        Args:
            A: int
            B: int
        
        Return: int
        """
        return max(self.values[A - 1: B])
    
    def U(self, A, B):
        """
        Args:
            A: int
            B: int
        """
        self.values[A - 1] = B

        
def get_input():
    return (int(x) if x.isdigit() else x for x in input().split())


def main():
    _, M = get_input()
    values = list(get_input())
    solution = Solution(values)

    for _ in range(M):
        C, A, B = get_input()
        if C == "Q":
            print(solution.Q(A, B))
        elif C == "U":
            solution.U(A, B)

if __name__ == "__main__":
    main()
