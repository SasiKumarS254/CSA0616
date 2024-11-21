def count_indices(nums1, nums2):
    set2 = set(nums2)
    answer1 = sum(num in set2 for num in nums1)
    answer2 = sum(num in nums1 for num in nums2)
    return [answer1, answer2]
nums1 = [2, 3, 2]
nums2 = [1, 2]
print(count_indices(nums1, nums2))  
