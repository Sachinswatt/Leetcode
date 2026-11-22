class Solution(object):
    def isPalindrome(self, x):
        x = str(x)
        pal = ""

        for i in x:
            pal = i + pal

        if x == pal:
            return True
        else:
            return False
    