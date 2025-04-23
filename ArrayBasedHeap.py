class Item:
    def __init__(self, key, value):
        self.value =value 
        self.key = key 

class ArrayBasedHeap:
    def __init__(self):
        self.data = []
        self.data.append(None)

    def add(self,key,value):
        self.data.append(Item(key,value))
        self.upHeap()

    def min(self):
        item = self.data[1]
        return (item.key, item.value)
    
    def remove_min(self):
        self.data[1], self.data[len(self.data)-1] = self.data[len(self.data)-1], self.data[1]
        self.data.pop()
        self.downHeap()
        
    def downHeap(self):
        n =  1
        while n * 2 < len(self.data):  # 자식이 존재할 때만 실행
                left = n * 2
                right = n * 2 + 1
                small = left

                # 오른쪽 자식이 존재하고, 오른쪽 자식이 더 작으면 small을 right로 설정
                if right < len(self.data) and self.data[right].key < self.data[left].key:
                    small = right

                # 부모가 더 작거나 같으면 멈춤 (힙 조건 만족)
                if self.data[n].key <= self.data[small].key:
                    break

                # swap 후 이동
                self.data[n], self.data[small] = self.data[small], self.data[n]
                n = small

    
    def upHeap(self):
        n = len(self.data) - 1
        while n>1 and self.data[n].key < self.data[n//2].key:
            self.data[n], self.data[n//2] = self.data[n//2], self.data[n]
            n = n//2


a = ArrayBasedHeap()

a.add(3,10)
a.add(4,11)
a.add(1,5)
a.add(6,235)

print(a.data[1].value)
a.remove_min()
print(a.data[1].value)



    
        
