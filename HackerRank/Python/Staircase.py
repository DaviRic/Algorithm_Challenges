def staircase(n):
    i = 1
    for i in range(1, n):
        print(f"' '*{(i-1)}'#'")