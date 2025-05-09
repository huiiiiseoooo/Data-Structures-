
from random import randrange
class item():
    def __init__(self, key, value):
        self.key = key 
        self.value = value

class HashMapBase():
    def __init__(self, cap = 11, p =109345121):
        self.cap = cap
        self.table = cap*[None]
        self.n =0 
        self.prime = p
        self.scale = 1 + randrange(p-1)
        self.shift = randrange(p)
        
    def hashfunction(self,k):
        return ((hash(k)*self.scale + self.shift )% self.prime % self.cap)

    def len(self):
        return self.n
    
    def getitem(self,k):
        h = self.hashfunction(k)
        item = self.table[h]
        if item.key != k:
            raise KeyError("key가 존재하지않습니다")
        return item.value
    
        
    def setitem(self, k, v):
        key = self.hashfunction(k)
        self.table[key] = item(k, v)
        self.n +=1

    def delitem(self, k):
        key = self.hashfunction(k)
        item = self.table[key]
        if item.key == k:  
            self.table[key] = None
        else:
            raise KeyError("key값이 없습니다")


hm = HashMapBase()

hm.setitem('apple', 10)
hm.setitem('banana', 20)
hm.setitem('cherry', 30)

print(hm.getitem('apple'))    # ➤ 10
print(hm.getitem('banana'))

hm.delitem('apple')

