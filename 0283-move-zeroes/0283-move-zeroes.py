class Solution(object):
    def moveZeroes(self, nums):
        arr1 = []
        arr2 = []
        for i in range(len(nums)):
            if nums[i] == 0:
                arr2.append(nums[i])
            else:
                arr1.append(nums[i])
        nums[:] =  arr1+arr2