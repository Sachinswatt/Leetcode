class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        l = nums1 + nums2
        l.sort()
        n = len(l)
        if n % 2 != 0:
            return l[n//2]
        else:
            return (l[n//2-1]+l[n//2])/2.0