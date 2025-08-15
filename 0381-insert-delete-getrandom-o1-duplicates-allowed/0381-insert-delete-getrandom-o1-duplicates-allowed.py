import random
class RandomizedCollection:

    def __init__(self):
        self.array=[]
        self.map={}

    def insert(self, val: int) -> bool:
        first_time=val not in self.map
        if first_time:
            self.map[val]=set()
        self.array.append(val)
        self.map[val].add(len(self.array)-1)
        return first_time

    def remove(self, val: int) -> bool:
        if val not in self.map:
            return False
        index = self.map[val].pop()
        last_el=self.array[-1]
        if index!=len(self.array)-1:

            self.array[index]=last_el
            self.map[last_el].remove(len(self.array)-1)
            self.map[last_el].add(index)
        self.array.pop()
        
        if not self.map[val]:
            del self.map[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.array)


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()