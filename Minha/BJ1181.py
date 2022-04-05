n = int(input())
tl = [input() for i in range(n)]

tl = list(set(tl))
tl= sorted(tl)
tl.sort(key=len)
for i in range(len(tl)):
    print(tl[i])