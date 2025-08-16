class Solution:
    def binarySubstring(self, s):
        #code here
        one=0
        for i in s:
            if i=='1':
                one+=1
        return (one*(one-1))//2