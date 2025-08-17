class Solution:
    def missingNum(self, arr):
        # code here
        l=len(arr)+1
        total=(l*(l+1))//2
        count=0
        for i in arr:
            count+=i
        return total -count