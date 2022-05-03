def solution(n, lost, reserve):
    answer = 0
    lostlen = len(lost)     
    for i in range(len(reserve)):       
        if(lost.count(reserve[i])) > 0:     
            del lost[lost.index(reserve[i])]    
            reserve[i]=-1   
            answer+=1 
    for i in range(reserve.count(-1)):  
        reserve.remove(-1)
    for i in range(len(reserve)):
        for j in range(len(lost)):
            if  reserve[i]-1 <= lost[j] <= reserve[i]+1:
                answer+=1
                break
            print(answer)
    if answer >= lostlen:
        answer = n
    else:
        answer = n-lostlen+answer
    return answer
