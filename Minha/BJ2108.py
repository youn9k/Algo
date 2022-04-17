import statistics as st
n = int(input())
lst = []
for i in range(n):
    lst.append(int(input()))
slst = sorted(lst)
'''
cb = 0
cnt={}
for i in slst:
    if i not in cnt.keys():
        cnt[i] = 1
    else:
        cnt[i] +=1

cl=[]
for i in cnt:
    if cb<cnt[i]:
        cb = cnt[i]
        cl.clear()
        cl.append(i)
    elif cb==cnt[i]:
        cl.append(i)
'''

cl = st.multimode(slst)
print(int(round(sum(lst)/n, 0)))
print(slst[int(n/2)])
print(cl[0] if len(cl)==1 else cl[1])
print(slst[-1]-slst[0])

#최빈값은 statistics모듈이 더 간결하긴 한데 메모리랑 시간은 더 드네용