class Solution(object):
    def generateParenthesis(self, n):
        result = []

        def backtrack(curr, open_count, close_count):
            if len(curr) == 2 * n:
                result.append(curr)
                return

            # Add '(' if we still can
            if open_count < n:
                backtrack(curr + "(", open_count + 1, close_count)

            # Add ')' only if it won't make the string invalid
            if close_count < open_count:
                backtrack(curr + ")", open_count, close_count + 1)

        backtrack("", 0, 0)
        return result