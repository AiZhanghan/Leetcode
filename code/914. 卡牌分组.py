from collections import Counter


class Solution:
    def hasGroupsSizeX(self, deck):
        """
        Args:
            deck: list[int]

        Return:
            bool
        """
        counter = Counter(deck)
        min_counter = min(counter.values())
        if min_counter < 2:
            return False
        
        primes = []
        mark = [False for _ in range(min_counter + 1)]
        for i in range(2, min_counter + 1):
            if mark[i]:
                continue
            primes.append(i)
            j = i + i
            while j < min_counter + 1:
                mark[j] = True
                j += i
        
        for v in primes:
            if len(deck) % v:
                continue
            flag = True
            for val in counter.values():
                if val % v:
                    flag = False
                    break
            if flag:
                return True
        
        return False


# class Solution:
#     def hasGroupsSizeX(self, deck):
#         """
#         Args:
#             deck: list[int]

#         Return:
#             bool
#         """
#         counter = Counter(deck)
#         for i in range(2, min(counter.values()) + 1):
#             if len(deck) % i:
#                 continue
#             for j, value in enumerate(counter.values()):
#                 if value % i:
#                     break
#             if j == len(counter) - 1 and list(counter.values())[-1] % i == 0:
#                 return True
#         return False