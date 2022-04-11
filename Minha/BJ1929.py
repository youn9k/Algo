n1,n2 = map(int, input().split())

lst = [True]*(n2+1)
lst[0] = lst[1]=False
for a in range(len(lst)):
    if lst[a]:
        for b in range(a*2, n2+1, a):
            lst[b]=False
        if(a>=n1): print(a)
'''
for i in range(n1, n2+1):
    flag = True
    if i<=3: print(i)
    if i%2==0 or i%3==0:
        flag = False
    else:
        for j in range(2, i):
            if (i % j) == 0:
                flag = False
                break
    if(flag): print(i)
'''
#에라토스테네스의 체를 쓰면 소수를 구할 때 시간복잡도 감소