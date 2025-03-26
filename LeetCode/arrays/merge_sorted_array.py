def merge(nums1, m, nums2, n):
    index = m
    index_nums2 = 0
    while index < len(nums1):
        nums1[index] = nums2[index_nums2]
        index+=1
        index_nums2+=1
    nums1.sort()

nums1 = [1,2,3,0,0,0]
nums2 = [5,4,6]
merge(nums1, 3, nums2, 3)
print(nums1)