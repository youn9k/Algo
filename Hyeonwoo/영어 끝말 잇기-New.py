def solution(n, words):
    old = []
    cnt = 0
    for x in words:
        if len(old)>=1:
            tmp = old[len(old)-1]
            if tmp[len(tmp)-1] != x[0]:
                return [cnt%n+1, words.index(x, words.index(x))//n+1]
            if x in old:
                return [cnt%n+1, words.index(x, words.index(x)+1)//n+1]
        old.append(x)
        cnt+=1
    return [0,0]