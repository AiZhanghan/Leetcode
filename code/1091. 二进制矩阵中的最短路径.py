from collections import deque


class Solution:
    def shortestPathBinaryMatrix(self, grid):
        """
        Args:
            grid: list[list[int]]

        Return:
            int
        """
        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1

        directs = [
            [1, 0],
            [1, 1],
            [1, -1],
            [-1, 0],
            [-1, 1],
            [-1, -1],
            [0, 1],
            [0, -1]
        ]
        visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
        
        queue = deque()
        queue.append((0, 0, 1))
        visited[0][0] = True

        while queue:
            x, y, path = queue.popleft()
            print(x, y, path)
            if x == len(grid) - 1 and y == len(grid[0]) - 1:
                return path
            for dx, dy in directs:
                new_x = x + dx
                new_y = y + dy
                # if new_x == len(grid) - 1 and new_y == len(grid[0]) - 1:
                #     return path + 1
                if 0 <= new_x < len(grid) and 0 <= new_y < len(grid[0]) \
                    and grid[new_x][new_y] == 0 and not visited[new_x][new_y]:
                    visited[new_x][new_y] = True
                    queue.append((new_x, new_y, path + 1))
        return -1


# if __name__ == "__main__":
#     grid = [[0,0,0],[1,0,0],[1,1,0]]
#     print(Solution().shortestPathBinaryMatrix(grid))
