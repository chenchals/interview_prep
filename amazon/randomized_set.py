import random
class RandomizedSet(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.list = []
        self.location = {}

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.location:
            return False
        self.list.append(val)
        idx = len(self.list)-1
        self.location[val] = idx
        return True

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.location:
            return False
        idx = self.location[val]
        last = self.list[-1]
        # swap value of last and target
        self.list[idx] = last
        # update last with new location
        self.location[last] = idx
        self.list.pop()
        self.location.pop(val)
        # how to delete, constant time deletion with list (pop tail, swap value between tail and val
        return True


    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        idx = random.randint(0, len(self.location)-1)
        ret = self.list[idx]
        return ret



# # Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(1)
# param_2 = obj.remove(2)
# param_3 = obj.getRandom()
# print(param_3)