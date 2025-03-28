def containsDuplicate(nums):
    count_reps = {}
    for i, num in enumerate(nums):
        if num in count_reps:
            count_reps[num].append(i)
            return True
        else:
            count_reps[num] = [i]
    return False

nums = [1,2,3,3]
print(containsDuplicate(nums))