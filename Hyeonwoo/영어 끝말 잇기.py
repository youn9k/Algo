from cgitb import reset


n = 3
words = ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]
#words = ["land", "dream", "mom", "mom", "ror"]
#words = ["land", "dream", "mom", "mom"]
#words = ["abb", "baa", "ccc", "cda", "abb"]
#words = ['qwe', 'eqwe', 'eqwe']

def solution(n, words):
    newDict = dict()
    resetNum = 1
    checkWord = ""
    resultX = 0
    resultY = 0


    for i in range (0, len(words)-1):
        if (words[i][-1] != words[i+1][0]):
            checkWord = words[i+1]
            break

    if (checkWord == ""): 
        for i in words:
            if (words.count(i) >= 2):
                checkWord = i
                break

    for i in range (1, n+1):
        newDict[i] = []

    for i in words:
        if (resetNum > n):
            resetNum = 1
        newDict[resetNum].append(i)
        resetNum += 1
    
    for i in range (len(newDict), 0, -1):
        if (checkWord in newDict[i]):
            resultX = i
            resultY = newDict[i].index(checkWord) + 1
            break

    return([resultX, resultY])


