def moveZeroes(nums):
    i = 0
    k = 1
    aux = 0
    while i < len(nums):
        if k < len(nums) - 1 and nums[i] == 0 and nums[k] != 0:
            aux = nums[i]
            nums[i] = nums[k]
            nums[k] = aux
            i+=1
            k+=1
        else:
            k+=1