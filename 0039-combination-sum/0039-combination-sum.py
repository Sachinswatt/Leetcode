class Solution(object):
    def combinationSum(self, candidates, target):
        ans = []

        def solve(index, arr):
            s = sum(arr)

            if s == target:
                ans.append(arr[:])
                return

            if s > target:
                return

            for i in range(index, len(candidates)):
                arr.append(candidates[i])
                solve(i, arr)      # same element can be used again
                arr.pop()          # remove last element

        solve(0, [])
        return ans