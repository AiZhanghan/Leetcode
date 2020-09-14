def word_count(filename, s):
    """
    Args:
        filename: str
        s: str
    
    Return:
        int
    """
    res = 0
    with open(filename) as f:
        for line in f.readlines():
            res += line.count(s)
    return res


if __name__ == "__main__":
    filename = r"./test.txt"
    res = word_count(filename, "a")
    print(res)