import random


class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dic = {}
        self.vector = []

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        
        Args:
            val: int
        
        Return:
            bool
        """
        if val not in self.dic:
            self.dic[val] = len(self.vector)
            self.vector.append(val)
            return True
        return False

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        
        Args:
            val: int
        
        Return:
            bool
        """
        if val in self.dic:
            last_element = self.vector[-1]
            index = self.dic[val]
            self.vector[index] = last_element
            self.dic[last_element] = index
            self.vector.pop()
            self.dic.pop(val)
            return True
        return False

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return random.choice(self.vector)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()