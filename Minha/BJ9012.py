n = int(input())

vb = []
for i in range(n):
    ps = input()
    x=0
    y=0
    psb = "YES"
    for j in range(len(ps)):
        if ps[j] == "(":
            x+=1
        elif ps[j] == ")":
            y+=1
        if x < y:
            psb = "NO"
            break
    if x != y:
        psb = "NO"
    vb.append(psb)

for i in range(n):
    print(vb[i])