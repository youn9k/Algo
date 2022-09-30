import sys

def solution(n):
    answer = 0
    numCount = bin(n).count("1")
    
    for i in range (n+1, 1_000_001):
        tempCount = bin(i).count("1")
    
        if (tempCount == numCount):
            answer = i
            break   
    return answer