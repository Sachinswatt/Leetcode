class Solution(object):
    def findNumbers(self, nums):
        count = 0
        for i in range(len(nums)):
            i = str(nums[i])
            if len(i) % 2 == 0:
                count += 1

        return (count)
  