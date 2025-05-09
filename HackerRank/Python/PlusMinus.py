def plusMinus(arr):
    positive = 0
    negative = 0
    zero = 0
    for i in arr:
        if i > 0:
            positive += 1
        if i < 0:
            negative += 1
        if i == 0:
            zero += 1
    
    array = []
    array.append(positive)
    array.append(negative)
    array.append(zero)
    for j in array:
        print(j/len(arr))