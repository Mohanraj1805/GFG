#User function Template for python3

class Solution:
    def findIndex (self,arr, key ):
        #code here.
        l=[]
        for i in range(0,len(arr)):
            if arr[i]==key:
                l.append(i)
        if len(l)==1:
            l.append(l[0])
        elif len(l)==0:
            l=[-1,-1]
        else:
            l=[l[0],l[-1]]
        return l