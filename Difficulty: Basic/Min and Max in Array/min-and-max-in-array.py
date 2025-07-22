#User function Template for python3
#User function Template for python3

class Solution:
    def get_min_max(self, arr):
    
        n=len(arr)
        if n==0:
            raise ValueError('empty error')
        if n==1:
            return arr[0],arr[0]
        if arr[0]<arr[1]:
            l,h=arr[0],arr[1]
        else:
            l,h=arr[1],arr[0]
        i=2
        while i < n-1:
            if arr[i]<arr[i+1]:
                l=min(l,arr[i])
                h=max(h,arr[i+1])
            else:
                l=min(l,arr[i+1])
                h=max(h,arr[i])
            i+=2
        if n%2==1:
            l=min(l,arr[-1])
            h=max(h,arr[-1])
        return l,h
        
        # l=arr[0]
        # h=arr[0]
        # for i in arr:
        #     if i < l:
        #         l=i
        #     elif i > h:
        #         h=i
        # return l,h
        # n=len(arr)
        # if n==0:
        #     raise ValueError('empty error')
        # if n==1:
        #     return arr[0],arr[0]
        # if arr[0]<arr[1]:
        #     l,h = arr[0],arr[1]
        # else:
        #     l,h=arr[1],arr[0]
        # i=2
        # while i<n-1:
        #     if arr[i]<arr[i+1]:
        #         l=min(l,arr[i])
        #         h=max(h, arr[i+1])
        #     else:
        #         l=min(l, arr[i+1])
        #         h=max(h, arr[i])
        #     i+=2
        # if n%2==1:
        #     l=min(l,arr[-1])
        #     h=max(h,arr[-1])
        # return l,h

    