class Solution:
    def canMeasureWater(self, x, y, z):
        """
        Args:
            x: int
            y: int
            z: int
        
        Return:
            bool
        """
        stack = [(0, 0)]
        seen = set()
        while stack:
            remain_x, remain_y = stack.pop()
            if remain_x == z or remain_y == z or remain_x + remain_y == z:
                return True
            if (remain_x, remain_y) in seen:
                continue
            seen.add((remain_x, remain_y))
            stack.append((x, remain_y))
            stack.append((remain_x, y))
            stack.append((0, remain_y))
            stack.append((remain_x, 0))
            stack.append((remain_x - min(remain_x, y - remain_y), 
                          remain_y + min(remain_x, y - remain_y)))
            stack.append((remain_x + min(remain_y, x - remain_x), 
                          remain_y - min(remain_y, x - remain_x)))
        return False
        