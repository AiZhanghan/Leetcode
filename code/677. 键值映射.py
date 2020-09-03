class MapSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {}

    def insert(self, key, val):
        """
        Args:
            key: str
            val: int
        """
        node = self.root
        for c in key:
            if c not in node:
                node[c] = {}
            node = node[c]
        node["val"] = val

    def sum(self, prefix):
        """
        Args:
            prefix: str
        
        Return:
            int
        """
        node = self.root
        for c in prefix:
            if c not in node:
                return 0
            node = node[c]
        res = 0

        def dfs(node):
            for c in node:
                if c == "val":
                    nonlocal res
                    res += node[c]
                else:
                    dfs(node[c])
        
        dfs(node)
        return res       


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)