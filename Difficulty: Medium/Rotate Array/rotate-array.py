#User function Template for python3

class Solution:
    #Function to rotate an array by d elements in counter-clockwise direction. 
    def rotateArr(self, arr, d):
        #Your code here
        d=d%len(arr)
        def rotate(l,r):
            while l < r:
                arr[l],arr[r]=arr[r],arr[l]
                l+=1
                r-=1
        rotate(0,d-1)
        rotate(d,len(arr)-1)
        rotate(0,len(arr)-1)
        return arr