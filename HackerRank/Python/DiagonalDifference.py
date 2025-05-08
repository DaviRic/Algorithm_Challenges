def diagonalDifference(arr):
    right_to_left = 0
    left_to_right = 0
    for i in range(len(arr)): # Linha
        for j in range(len(arr)): # Coluna
            if i == j:
                left_to_right += arr[i][j]
            if i + j == len(arr) - 1:
                right_to_left += arr[i][j]
    return abs(left_to_right-right_to_left)
