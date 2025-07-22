# User function Template for python3

class Solution:
    # Function to check if two arrays are equal or not.
    def checkEqual(self, a, b) -> bool:
        #code here
        
        # flag=True
        # for i in a:
        #     if i in b:
        #         continue
        #     else:
        #         flag=False
        # return flag
        n,m=len(a),len(b)
        if n!=m:
            return False
        mp={}
        for i in a:
            mp[i]=mp.get(i,0)+1
        for j in b:
            if j not in mp:
                return False
            if mp[j] == 0: 
                return False
            mp[j]-=1
        return True
        