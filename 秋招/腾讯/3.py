from collections import Counter


class Solution:
    def func(self, strings, K):
        """
        Args:
            strings: list[str]
            K: int
        """
        counter = Counter(strings)
        counter_list = [(key, counter[key]) for key in counter]
        # 频数大, 字母序小 -> 频数小, 字母序大
        counter_list.sort(key=lambda x: [-x[1], x])
        for i in range(K):
            print(counter_list[i][0], counter_list[i][1])
        
        counter_list.sort(key=lambda x: [x[1], x])
        for i in range(K):
            print(counter_list[i][0], counter_list[i][1])


if __name__ == "__main__":
    N, K = list(map(int, input().split()))
    strings = []
    for _ in range(N):
        strings.append(input())
    Solution().func(strings, K)