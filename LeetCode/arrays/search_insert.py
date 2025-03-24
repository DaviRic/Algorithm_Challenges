def searchInsert(nums, target):
    count = 0
    for number in nums:
        if number == target:
            return count
        count+=1
    count = 1
    for i in range(len(nums)):
        if target > nums[-1]:
            count = len(nums)
            return count
        elif target <= nums[0]:
            count = 0
            return count
        if nums[i] < target and nums[i+1] >= target:
            return count
        count+=1

nums = [1,3,5,6]
searchInsert(nums, 7)