class Solution:
    def hammingDistance(self, x, y):
        """
        Args:
            x: int
            y: int
        
        Return:
            int
        """
        xor = x ^ y
        distance = 0
        while xor:    
            distance += 1
            xor = xor & (xor - 1)
        return distance


# class Solution:
#     def hammingDistance(self, x: int, y: int) -> int:
#         """
#         Args:
#             x: int
#             y: int
        
#         Return:
#             int
#         """
#         xor = x ^ y
#         distance = 0
#         while xor:
#             if xor & 1:
#                 distance += 1
#             xor = xor >> 1
#         return distance


# class Solution:
#     def hammingDistance(self, x: int, y: int) -> int:
#         """
#         Args:
#             x: int
#             y: int
        
#         Return:
#             int
#         """
#         return bin(x ^ y).count("1")
