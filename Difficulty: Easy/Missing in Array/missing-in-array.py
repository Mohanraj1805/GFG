class Solution:
    def missingNum(self, arr):
        # code here
        n=len(arr)+1
        count=n*(n+1)//2
        arr_c=0
      
        for i in arr:
            arr_c+=i
        return count-arr_c