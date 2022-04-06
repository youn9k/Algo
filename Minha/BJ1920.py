n = int(input())
a=list(map(int, input().split()))
a=sorted(a)
m = int(input())
b=list(map(int, input().split()))

for i in range(m):
    start = 0
    end = len(a)-1
    bol = 0
    while start <= end:
        mid = (start + end) // 2
    
        if a[mid] == b[i]: 
            bol = 1
            break
        elif a[mid] < b[i]: 
            start = mid + 1
        else: 
            end = mid - 1
    print(bol)
    
#***이진탐색***