class Solution:
    def search(self,arr, x):
        #code here
        # l=0
        # r=len(arr)-1
        # while l <= r:
        #     mid=(l+r)//2
        #     if arr[mid]==x:
        #         return mid 
        #     elif arr[mid] < x :
        #         l=mid+1
        #     else:
        #         r= mid-1
        # return -1
        for i in range(len(arr)):
            if arr[i]==x:
                return i
        return -1
            