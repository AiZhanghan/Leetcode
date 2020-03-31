class Solution:
    def findWhetherExistsPath(self, n, graph, start, target):
        """
        parameter:
            n: int
            graph: list[list[int]]
            start: int
            target: int
        return: bool
        """
        self.graph_dict = dict()
        for key, value in graph:
            if key not in self.graph_dict:
                self.graph_dict[key] = {value}
            else:
                self.graph_dict[key].add(value)
        
        self.visited = [False for _ in range(n)]
        if start not in self.graph_dict:
            return False
        
        return self.dfs(start, target)

    def dfs(self, start, target):
        """
        parameter:
            start: int
            target: int
        return bool
        """
        if start == target:
            return True
        
        self.visited[start] = True
        res = False
        if start in self.graph_dict:
            for next_node in self.graph_dict[start]:
                if res:
                    break

                if not self.visited[next_node]:
                    res = self.dfs(next_node, target)
        return res
