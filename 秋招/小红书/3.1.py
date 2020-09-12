class Solution:
    def func(self, boxes):
        """
        Args:
            boxes: list[int]
        
        Return:
            int
        """
        if not boxes:
            return 0
        boxes = self.more_boxes(boxes)
        boxes.sort(reverse=True)
        dp = [boxes[i][2] for i in range(len(boxes))]
        # dp[0] = boxes[0][2]
        for i in range(1, len(dp)):
            box = boxes[i]
            for j in range(i):
                if self.can_add(boxes, i, j):
                    dp[i] = max(dp[i], dp[j] + box[2])
        return max(dp)
    
    def can_add(self, boxes, i, j):
        if boxes[i][0] >= boxes[j][0] or boxes[i][1] >= boxes[j][1]:
            return False
        return True

    def more_boxes(self, boxes):
        """
        Args:
            boxes: list[int]
        
        Return:
            list[int]
        """
        res = []
        for box in boxes:
            box.sort()
            a, b, c = box
            res.append([a, b, c])
            res.append([a, c, b])
            res.append([b, c, a])
        return res


if __name__ == "__main__":
    while True:
        N = input()
        if N == "":
            break

        N = int(N)
        boxes = []
        for _ in range(N):
            boxes.append(list(map(int, input().split())))
        solver = Solution()
        res = solver.func(boxes)
        print(res)
    # boxes = [
    #     [4, 2, 5],
    #     [3, 1, 6],
    #     [3, 2, 1],
    #     [6, 3, 9],
    # ]
    # boxes = [
    #     [4, 5, 6],
    #     [3, 1, 6],
    #     [3, 2, 1],
    # ]
    # solver = Solution()
    # res = solver.func(boxes)
    # print(res)