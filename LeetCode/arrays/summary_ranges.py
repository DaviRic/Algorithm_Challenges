def summaryRanges(nums):
    if not nums:
        return [] 
    result = []
    start = nums[0]
    for i in range(1, len(nums)):
        if nums[i] != nums[i-1] + 1:
            if start == nums[i-1]:
                result.append(str(start))
            else:
                aux = f'{start}->{nums[i-1]}'
                result.append(aux)
            start = nums[i]
    if start == nums[-1]:
        result.append(str(start))
    else:
        aux = f'{start}->{nums[-1]}'
        result.append(aux)
    return result

print(summaryRanges(nums = [0,1,2,4,5,7]))
