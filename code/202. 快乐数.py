class Solution:
    def isHappy(self, n):
        """
        Args:
            n: int
        
        Return:
            bool
        """
        fast = self.helper(self.helper(n))
        slow = self.helper(n)
        while slow != fast:
            fast = self.helper(self.helper(fast))
            slow = self.helper(slow)
        return slow == 1

    def helper(self, n):
        """
        Args:
            n: int
        
        Return:
            int
        """
        res = 0
        while n:
            res += (n % 10) ** 2
            n //= 10
        return res
    

# class Solution:
#     def isHappy(self, n):
#         """
#         Args:
#             n: int
        
#         Return:
#             bool
#         """
#         res = True
#         visited = set()

#         while n != 1:
#             n = self.helper(n)
#             if n in visited:
#                 res = False
#                 break
#             else:
#                 visited.add(n)
        
#         return res

#     def helper(self, n):
#         """
#         Args:
#             n: int
        
#         Return:
#             int
#         """
#         res = 0
#         while n:
#             res += (n % 10) ** 2
#             n //= 10
#         return res
    

if __name__ == "__main__":
    n = 19
    print(Solution().isHappy(n))
