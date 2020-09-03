class Solution:
    def func(self, m, k, gifts):
        """
        Args:
            m: int
            k: int
            gifts: list[int]
        
        Return:
            int
        """
        res = 0
        # 礼物按心动值和价格排序
        gifts.sort(key=lambda x: [-x[2], x[0], x[1]])
        for price, weight, _ in gifts:
            if price <= k and weight <= m:
                res += 1
                k -= price
                m -= weight
        return res


if __name__ == "__main__":
    n, m, k = list(map(int, input().split()))
    gifts = []
    for _ in range(n):
        gifts.append(list(map(int, input().split())))
    res = Solution().func(m, k, gifts)
    print(res)
