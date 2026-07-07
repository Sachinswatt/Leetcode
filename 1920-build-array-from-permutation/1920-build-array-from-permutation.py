class Solution(object):
    def buildArray(self, nums):
        ans = []
        for i in range(len(nums)):
            ind = nums[nums[i]]
            ans.append(ind)
        return ans

        