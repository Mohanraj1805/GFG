class Solution:
    # Function to sort an array of 0s, 1s, and 2s
    def sort012(self, arr):
        # code here
        
        # for i in range(len(arr)):
        #     for j in range(0,len(arr)-1):
        #         if arr[j] > arr[j+1]:
        #             arr[j],arr[j+1]=arr[j+1],arr[j]
        # return arr
        count0=0
        count1=0
        count2=0
        for i in arr:
            if i==0:
                count0+=1
            elif i==1:
                count1+=1
            else:
                count2+=1
        idx=0
        for i in range(count0):
            arr[idx]=0
            idx+=1
        for i in range(count1):
            arr[idx]=1
            idx+=1
        for i in range(count2):
            arr[idx]=2
            idx+=1
        return arr
        