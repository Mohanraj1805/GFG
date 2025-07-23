class Solution:
    def findTriplets(self, arr):
        #code here
        arr.sort()
        n=len(arr)
        for i in range(n-2):
            l=i+1
            r=n-1
            while l<r:
                ans=arr[i]+arr[l]+arr[r]
                if ans==0:
                    return True
                elif ans >0:
                    r-=1
                else:
                    l+=1
        return False