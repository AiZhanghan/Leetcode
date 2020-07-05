class Solution:
    def isAdditiveNumber(self, num):
        """
        Args:
            num: str

        Return:
            bool
        """
        if len(num) < 3:
            return False
        
        for i in range(len(num) // 2):
            a = num[: i + 1]
            if a != "0" and a.startswith("0"):
                break
            
            for j in range(i + 1, len(num)):
                b = num[i + 1: j + 1]
                if b != "0" and b.startswith("0"):
                    break
                
                fib = [int(a), int(b)]
                k = j + 1
                while k < len(num):
                    nxt = fib[-1] + fib[-2]
                    nxt_str = str(nxt)
                    if num[k:].startswith(nxt_str):
                        k += len(nxt_str)
                        fib.append(nxt)
                    else:
                        break
                if k == len(num) and len(fib) > 2:
                    return True
        return False