class item:
    def __init__(self, key, value):
        self.key = key
        self.value = value


class UnsortedTableMap:
    def __init__(self):
        self.mapList = []

    def setitem(self, k, v):
        for i in self.mapList:
            if(i.key == k):
                i.value = v
                return
        self.mapList.append(item(k,v))
    
    def getitem(self,k):
        for i in self.mapList:
            if(i.key == k):
                return i.value
        raise KeyError("key를 찾을수 없습니다")
    
    def delitem(self, k):
        count = 0
        for i in self.mapList:
            if(i.key == k):
                self.mapList.pop(count)
            count +=1

    
    def len(self):
        return len(self.mapList)
    
utm = UnsortedTableMap()

utm.setitem(1,10)
utm.setitem(4,40)
utm.setitem(3,30)

print(utm.getitem(4))
print(utm.getitem(3))

print(utm.delitem(4))
