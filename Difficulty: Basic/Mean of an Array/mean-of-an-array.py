#User function Template for python3

class Solution:
    def findMean(self, arr):
        # code here 
        n=len(arr)
        count=0
        
        for i in arr:
            count+=i
        return count//n