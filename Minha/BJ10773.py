n = int(input())
lst = []

for i in range(n):
    p = int(input())
    if p == 0:
        lst.pop()
    else:
        lst.append(p)

'''
i=0
for j in range(n):
    if lst[i]==0:
        del lst[i-1:i+1]
        i-=2
    i+=1
'''
print(sum(lst))