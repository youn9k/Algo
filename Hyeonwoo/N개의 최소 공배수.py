def solution(arr):
    num = max(arr)
    while True:
        checked = []
        for i in range (len(arr)):
            if (num % arr[i] == 0):
                checked.append("1")
            else:
                checked.append("0")
                break
        if ("0" not in checked):
            return num
        num += 1
