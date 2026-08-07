class Solution(object):
    def subsetsWithDup(self, nums):
        nums.sort()          # Sort to bring duplicates together
        ans = []

        def backtrack(start, subset):
            ans.append(subset[:])   # Add current subset

            for i in range(start, len(nums)):
                # Skip duplicates at the same level
                if i > start and nums[i] == nums[i - 1]:
                    continue

                subset.append(nums[i])
                backtrack(i + 1, subset)
                subset.pop()

        backtrack(0, [])
        return ans
        