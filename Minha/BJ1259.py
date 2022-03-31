ls = []
while True:
    bol = 'yes'
    num = str(input())
    if num == '0': break
    
    lum = len(num)-1
    for i in  range(0, int(len(num)/2)):
        if num[i] != num[lum]:
            bol = 'no'
        lum-=1
    ls.append(bol)
    
for i in range(0, len(ls)):
    print(ls[i])