def birthdayCakeCandles(candles):
    tallest = max(candles)
    count = 0
    for i in candles:
        if i == tallest:
            count += 1
    return count
