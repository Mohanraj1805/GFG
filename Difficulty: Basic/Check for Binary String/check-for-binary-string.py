# Return true if s is binary, else false
class Solution:
    def isBinary(self, s):
        #code here
        flag=True
        for i in range(len(s)):
            if s[i]=='1' or s[i]=='0':
                continue
            else:
                return False
        return flag