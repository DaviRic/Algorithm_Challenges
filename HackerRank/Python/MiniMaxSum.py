def miniMaxSum(arr):
    maximum = 0
    minimum = 0
    flag = 0
    for i in arr:
        if flag == 0:
            minimum += i
        if flag > 0 and flag < len(arr)-2:
            maximum += i
            minimum += i
        if flag == len(arr) - 1:
            maximum += i
    print(maximum, minimum)