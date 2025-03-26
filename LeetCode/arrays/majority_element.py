def majorityElement(nums):
    maority_quatity = len(nums)/2
    count, elected, i, j = 0, 0, 0, 0
    while i < len(nums):
        elected = nums[i]
        while j < len(nums):
            if nums[j] == elected:
                count += 1
            j+=1
        i+=1
        if count > maority_quatity:
            return elected