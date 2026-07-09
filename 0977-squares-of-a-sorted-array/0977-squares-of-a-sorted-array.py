class Solution(object):
    def sortedSquares(self, nums):
        arr = []
        for i in range(len(nums)):
            square = nums[i]**2
            arr.append(square)
        arr.sort()
        return arr
    