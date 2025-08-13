#User function Template for python3

class Solution:
     def reverseString(self, s: str) -> str:
        # code here
        s=list(s)
        l=0
        r=len(s)-1
        while l < r:
            s[l],s[r]=s[r],s[l]
            l+=1
            r-=1
        return ''.join(s)
        