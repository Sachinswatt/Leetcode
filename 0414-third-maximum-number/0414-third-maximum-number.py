class Solution(object):
    def thirdMax(self, nums):
        arr = []
        for i in range(len(nums)):
            nums = list(set(nums))
            nums.sort(reverse = True)
            if len(nums)>=3:
                return nums[2]
            return nums[0]
            
        
        