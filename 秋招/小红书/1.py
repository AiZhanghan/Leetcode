
#请完成下面这个函数，实现题目要求的功能
#当然，你也可以不按照下面这个模板来作答，完全按照自己的想法来 ^-^ 
#******************************开始写代码******************************


def findMin(tree):
    """
    Args:
        tree: list[int]
    
    Return:
        int
    """
    tree_set = set(tree)
    for i in range(1, len(tree) + 1):
        if i not in tree_set:
            return i


#******************************结束写代码******************************

if __name__ == "__main__":
    
    _tree_cnt = 0
    _tree_cnt = int(input())
    _tree_i=0
    _tree = []
    while _tree_i < _tree_cnt:
        _tree_item = int(input())
        _tree.append(_tree_item)
        _tree_i+=1

    
    res = findMin(_tree)

    print(str(res) + "\n")