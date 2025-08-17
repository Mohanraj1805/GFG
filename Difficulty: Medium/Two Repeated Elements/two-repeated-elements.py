class Solution:
    def twoRepeated(self, arr):
        # code here
        s={}
        l=[]
        for i in arr:
            if i in s:
                s[i]+=1
                if s[i]==2:
                    l.append(i)
            else:
                s[i]=1
        return l
            
