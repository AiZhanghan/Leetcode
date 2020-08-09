def func(n):
    """
    Args:
        n: int
    
    Return:
        int
    """
    res = 0
    while n:
        n &= n - 1
        res += 1
    return res

if __name__ == "__main__":
    while True:
        n = int(input())
        print(func(n))
        