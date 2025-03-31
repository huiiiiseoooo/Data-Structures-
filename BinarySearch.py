data = [10,20,30,40,50,60,70,80,90,98,100]

def BinarySearch(data, target, low, high):
    mid = (high + low)//2
    if data[mid]==target:
        return mid
    
    elif data[mid]<target:
        
        return BinarySearch(data, target, mid+1, high) #오른쪽 탐색 로우값 주의
        
        
    else:
        return BinarySearch(data, target, low, mid-1) #왼쪽 탐색 하이값 주의

    
print(BinarySearch(data, 40,0,len(data)-1))

    