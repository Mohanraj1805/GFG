class Solution:
    def findSum(self, s):
        #code here
        temp='0'
        ans=0
        for i in  s:
            if i.isdigit():
                temp+=i
            else:
                ans+=int(temp)
                temp='0'
        return ans+int(temp)
