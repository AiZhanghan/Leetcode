class Solution:
    def splitIntoFibonacci(self, S):
        """
        Args:
            S: str
        
        Return:
            list[int]
        """
        for i in range(min(10, len(S))):
            x = S[: i + 1]
            if x != "0" and x.startswith("0"):
                break

            a = int(x)
            for j in range(i + 1, min(i + 11, len(S))):
                y = S[i + 1: j + 1]
                if y != "0" and y.startswith("0"):
                    break
                b = int(y)
                fib = [a, b]
                k = j + 1
                while k < len(S):
                    _next = fib[-1] + fib[-2]
                    _next_str = str(_next)
                    if _next <= 2 ** 31 - 1 and S[k:].startswith(_next_str):
                        k += len(_next_str)
                        fib.append(_next)
                    else:
                        break
                if k >= len(S) and len(fib) >= 3:
                    return fib
        return []


if __name__ == "__main__":
    S = "17522"
    print(Solution().splitIntoFibonacci(S))