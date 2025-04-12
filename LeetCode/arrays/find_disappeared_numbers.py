def findDisappearedNumbers(nums):
    for num in nums:
        index = abs(num) - 1
        if nums[index] > 0:
            nums[index] *= -1

    return [i + 1 for i in range(len(nums)) if nums[i] > 0]

findDisappearedNumbers([1,2])

"""
(Lógica mal entendida)
def findDisappearedNumbers(nums):
    nums.sort()
    first = nums[0]
    result = []
    actual = 1
    sign = False
    if first > 1:
        while actual != first:
            result.append(actual)
            actual += 1
    else:
        for i in range(len(nums)):
            if i+1 < len(nums):
                diff = nums[i+1] - nums[i]
            if diff > 1:
                actual = nums[i]+1
                sign = True
                while actual != nums[i+1]:
                    result.append(actual)
                    actual = actual + 1
        if sign:
            return result
        else:
            return [nums[-1]+1]
    return result
"""