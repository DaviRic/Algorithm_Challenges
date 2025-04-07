def findMaxConsecutiveOnes(nums):
    count = 0
    max_consecutive = 0
    for i in range(len(nums)):
        if nums[i] == 1:
            count+=1
        if count > max_consecutive:
            max_consecutive = count
        if nums[i] != 1:
            count = 0
    return max_consecutive

print(findMaxConsecutiveOnes(nums = [1,0,1,1,0,1]))