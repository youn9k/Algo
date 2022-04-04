n = int(input())
num_list = list(map(int, input().split()))
nlt = sorted(num_list)
m = int(input())
ans = 0

if m < nlt[0]: 
    for i in range(1, m+1):
        for j in range(i+1, nlt[0]): ans+=1
        for k in range(i+1, m): ans-=1
            
for i in range(0, n):
    if nlt[i] < m < nlt[i+1]:
        for k in range(nlt[i]+1, m+1):
            for l in range(k+1, nlt[i+1]): ans+=1
            for j in range(k+1, m): ans-=1
        break
        
print(ans)

'''쓰레기문제 n이 S[0]보다 작은 경우 고려하라는 문구+예제 입력 없어서 이에 대한 반례찾기 너무 어려움'''