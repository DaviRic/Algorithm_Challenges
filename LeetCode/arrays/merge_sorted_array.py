def merge(nums1, m, nums2, n):
    index = m
    index_nums2 = 0
    while index < len(nums1):
        nums1[index] = nums2[index_nums2]
        index+=1
        index_nums2+=1
    nums1.sort()
