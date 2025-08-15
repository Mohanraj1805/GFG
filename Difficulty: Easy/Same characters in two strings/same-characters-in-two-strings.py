#User function Template for python3

class Solution:

    def sameChar(self, A, B):
        a=A.lower()
        b=B.lower()
        count=0
        for i in range(len(a)):
            if a[i] ==b[i]:
                count+=1
        return count
        # code here
