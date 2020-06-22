class Solution:
    def isRectangleOverlap(self, rec1, rec2):
        """
        Args:
            rec1: list[int]
            rec2: list[int]
        
        Return:
            bool
        """
        x_overlap = not (rec1[2] <= rec2[0] or rec2[2] <= rec1[0])
        y_overlap = not (rec1[3] <= rec2[1] or rec2[3] <= rec1[1])
        return x_overlap and y_overlap


# class Solution:
#     def isRectangleOverlap(self, rec1, rec2):
#         """
#         Args:
#             rec1: list[int]
#             rec2: list[int]
        
#         Return:
#             bool
#         """
#         center1 = [(rec1[0] + rec1[2]) / 2, (rec1[1] + rec1[3]) / 2]
#         center2 = [(rec2[0] + rec2[2]) / 2, (rec2[1] + rec2[3]) / 2]
#         x_limit = (rec1[2] - rec1[0]) / 2 + (rec2[2] - rec2[0]) / 2
#         y_limit = (rec1[3] - rec1[1]) / 2 + (rec2[3] - rec2[1]) / 2
#         res = False
#         if abs(center1[0] - center2[0]) < x_limit and \
#             abs(center1[1] - center2[1]) < y_limit:
#             res = True
#         return res