def containsNearbyDuplicate(nums, k):
    count_dups = {}

    for i, num in enumerate(nums):
        if num in count_dups and abs(i - count_dups[num]) <= k:
            return True

        count_dups[num] = i

    return False

nums = [1,0,1,1]
print(containsNearbyDuplicate(nums, 1))