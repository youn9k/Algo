from collections import deque

n = int(input())
lst = deque(range(1, n+1))

for i in range(n-1):
    lst.popleft()    
    lst.append(lst.popleft())
print(lst[0])

#파이썬에서 list로 큐나 덱을 구현하면 절대절대 안된다네요... 무적권 collections.deque