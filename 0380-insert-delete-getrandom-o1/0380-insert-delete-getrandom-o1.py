class RandomizedSet:

    def __init__(self):
        self.hash = {}
        self.array = []

    def insert(self, val: int) -> bool:
        
        if val in self.hash: return False
        self.array.append(val)
        self.hash[val] = len(self.array) - 1
        return True
        

    def remove(self, val: int) -> bool:
        if val in self.hash:
            idx = self.hash[val]
            last_element = self.array[-1]
            self.array[idx] = last_element
            self.hash[last_element] = idx
            self.array.pop()
            del self.hash[val]
            return True
    
        return False
        

    def getRandom(self) -> int:
        random_idx = random.randint(0, len(self.array) - 1)
        return self.array[random_idx]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()