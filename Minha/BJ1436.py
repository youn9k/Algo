mn='666'
fn = bn = 0
n=int(input())
if(n>1):
    for i in range(n):
        if str(fn)[-1] != '6':
            mn = str(fn)+'666'
            fn+=1
        else:
            if str(bn)[-1] != '9':
                mn = '666'+ str(bn)
                bn+=1
            else:
                fn+=1
                bn=0
        
print(mn)

#GG 다음을 기약한다 영화감독 숌 시펄