import random
class RandomizedSet:

    def __init__(self):
        self.array=[]
        self.map={}

    def insert(self, val: int) -> bool:
        if val in self.map:
            return False
        self.array.append(val)
        self.map[val]=len(self.array)-1
        return True 

    def remove(self, val: int) -> bool:
        if val not in self.map:
            return False
        index = self.map[val]
        last_el=self.array[-1]
        self.array[index]=last_el
        self.map[last_el]=index
        self.array.pop()
        del self.map[val]
        return True
               

    def getRandom(self) -> int:
        return random.choice(self.array)
        
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()