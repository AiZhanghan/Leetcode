class Solution:
    def func(self, boxes):
        """
        暴力回溯+排序剪枝

        Args:
            boxes: list[int]
        
        Return:
            int
        """
        if not boxes:
            return 0

        self.boxes = self.more_boxes(boxes)
        self.boxes.sort(reverse=True)
        self.res = 0
        self.dfs(0, [])
        return self.res

    def dfs(self, index, path):
        """
        Args:
            index: int
            path: list[list[int]]
        """
        if index == len(self.boxes):
            self.res = max(self.res, self.eval(path))
            return
        for cur_index in range(index, len(self.boxes)):
            cur_box = self.boxes[cur_index]
            if path and (cur_box[0] >= path[-1][0] or cur_box[1] >= path[-1][1]):
                continue
            path.append(cur_box)
            self.dfs(cur_index + 1, path)
            path.pop()

    def eval(self, path):
        """
        Args:
            path: list[list[int]]
        
        Return:
            int
        """
        res = 0
        for _, _, c in path:
            res += c
        return res

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
    # while True:
    #     try:
    #         N = int(input())
    #     except:
    #         break
    #     boxes = []
    #     for _ in range(N):
    #         boxes.append(list(map(int, input().split())))
    #     solver = Solution()
    #     res = solver.func(boxes)
    #     print(res)
    boxes = [
        [4, 2, 5],
        [3, 1, 6],
        [3, 2, 1],
        [6, 3, 9],
    ]
    solver = Solution()
    res = solver.func(boxes)
    print(res)