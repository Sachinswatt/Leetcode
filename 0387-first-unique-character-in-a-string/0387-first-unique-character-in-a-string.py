class Solution(object):
    def firstUniqChar(self, s):
        u = ""
        for char in s:
            if char not in u:
                u += char
        for char in u:
            if s.count(char)==1:
                return s.index(char)
        return -1