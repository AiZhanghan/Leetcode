class Solution:
    def func(self, x, y, commands):
        """
        Args:
            x: int
            y: int
            commands: str
        
        Return:
            x, y
        """
        for c in commands:
            if c == "U":
                y += 1
            elif c == "D":
                y -= 1
            elif c == "L":
                x -= 1
            elif c == "R":
                x += 1
        return x, y


if __name__ == "__main__":
    x, y = list(map(int, input().split()))
    commands = input()

    new_x, new_y = Solution().func(x, y, commands)
    print("%d %d" % (new_x, new_y))

