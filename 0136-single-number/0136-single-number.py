class Solution(object):
    def singleNumber(self, nums):
        arr = []
        for i in range(len(nums)):
            if nums[i] not in arr:
                arr.append(nums[i])
            else:
                arr.remove(nums[i])
        return arr[0]
        

        