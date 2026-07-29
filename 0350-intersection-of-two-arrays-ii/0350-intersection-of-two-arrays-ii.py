class Solution(object):
    def intersect(self, nums1, nums2):
        arr = []

        for i in range(len(nums1)):
            if nums1[i] in nums2:
                arr.append(nums1[i])
                nums2.remove(nums1[i])   # Remove one occurrence

        return arr