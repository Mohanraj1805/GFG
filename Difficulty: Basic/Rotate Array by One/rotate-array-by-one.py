#User function Template for python3

# class Solution:
#     def rotate(self, arr):
#         n=len(arr)-1
#         def help(i,j):
#             while i<j:
#                 arr[i], arr[j] = arr[j], arr[i]
#                 i += 1
#                 j-=1
#         help(0,n)
       
#         help(1,n)


#         return arr
        #User function Template for python3

class Solution:
    def rotate(self, arr):
        i, j = 0, len(arr) - 1
        while i != j:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
        return arr
        