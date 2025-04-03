def intersection(nums1, nums2):
    intersection_vector = []
    for i in range(len(nums1)):
        if nums1[i] in nums2:
            if nums1[i] not in intersection_vector:
                intersection_vector.append(nums1[i])
    return intersection_vector

intersection(nums1 = [4,9,5], nums2 = [9,4,9,8,4])