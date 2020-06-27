class Solution:
    def multiply(self, num1, num2):
        """
        Args:
            num1: str
            num2: str

        Return:
            str
        """
        if num1 == "0" or num2 == "0":
            return "0"
        res = [0 for _ in range(len(num1) + len(num2))]
        for i in reversed(range(len(num1))):
            n1 = ord(num1[i]) - ord("0")
            for j in reversed(range(len(num2))):
                n2 = ord(num2[j]) - ord("0")
                _sum = res[i + j + 1] + n1 * n2
                res[i + j + 1] = _sum % 10
                res[i + j] += _sum // 10
        result = ""
        for i in range(len(res)):
            if i == 0 and res[i] == 0:
                continue
            result += str(res[i])
        return result


# class Solution:
#     def multiply(self, num1, num2):
#         """
#         Args:
#             num1: str
#             num2: str

#         Return:
#             str
#         """
#         if num1 == "0" or num2 == "0":
#             return "0"
        
#         res = "0"
#         for i in reversed(range(len(num2))):
#             carry = 0
#             temp = ""
#             for j in range(len(num2) - 1 - i):
#                 temp += "0"
#             n2 = ord(num2[i]) - ord("0")
            
#             j = len(num1) - 1
#             while j >= 0 or carry != 0:
#                 n1 = ord(num1[j]) - ord("0") if j >= 0 else 0
#                 product = (n1 * n2 + carry) % 10
#                 temp += str(product)
#                 carry = (n1 * n2 + carry) // 10
#                 j -= 1
#             res = self.add_str(res, temp[::-1])
#         return res
    
#     def add_str(self, num1, num2):
#         """
#         Args:
#             num1: str
#             num2: str
        
#         Return:
#             str
#         """
#         res = ""
#         carry = 0
#         i = len(num1) - 1
#         j = len(num2) - 1
#         while i >= 0 or j >= 0 or carry != 0:
#             x = ord(num1[i]) - ord("0") if i >= 0 else 0
#             y = ord(num2[j]) - ord("0") if j >= 0 else 0
#             _sum = (x + y + carry) % 10
#             res += str(_sum)
#             carry = (x + y + carry) // 10
#             i -= 1
#             j -= 1
#         return res[::-1]


if __name__ == "__main__":
    num1 = "123"
    num2 = "45"
    print(Solution().multiply(num1, num2))