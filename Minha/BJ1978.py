n = int(input())
n_lst = list(map(int, input().split()))
n_lst.sort()
ans=0

flag = False
for i in range(n):
    if n_lst[i] < 2:
        continue
    flag = True
    for j in range(2, n_lst[i]):
        if (n_lst[i] % j) == 0:
            flag = False
            break
    if(flag): ans+=1

'''
lst = [True]*(n_lst[-1]+1)

lst[0] = lst[1]=False
for a in range(len(lst)):
    if lst[a]:
        for b in range(a*2, len(lst), a):
            lst[b]=False
        ans+=n_lst.count(a)
'''
print(ans)

#왜 이문제는 에라토스테네스의 체를 쓴 코드하고 단순검출방식하고 메모리 / 시간이 같을꼬 허허..