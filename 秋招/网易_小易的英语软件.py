class Solution:
    def __init__(self, scores):
        """
        Args:
            list[int]
        """
        self.scores = scores
        self.sorted_scores = sorted(scores)
    
    def query(self, index):
        """
        Args:
            index: int
        
        Return:
            float
        """
        target = self.scores[index - 1]
        left = 0
        right = len(self.sorted_scores) - 1
        while left <= right:
            mid = (left + right) // 2
            if self.sorted_scores[mid] <= target:
                left = mid + 1
            elif self.sorted_scores[mid] > target:
                right = mid - 1
        return ((left - 1) / len(self.scores)) * 100
    

if __name__ == "__main__":
    n = int(input())
    scores = list(map(int, input().split()))
    s = Solution(scores)
    query_num = int(input())
    for _ in range(query_num):
        index = int(input())
        print("%.6f" % s.query(index))

    # scores = [100, 98, 97]
    # s = Solution(scores)
    # print(s.query(1))