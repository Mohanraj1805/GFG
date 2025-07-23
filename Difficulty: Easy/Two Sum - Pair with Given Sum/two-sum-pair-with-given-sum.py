class Solution:
	def twoSum(self, arr, target):
	   # l=0
	   
	   # while l<len(arr):
	   #     r=l+1
	   #     while r<len(arr):
	   #         if arr[l]+arr[r]==target:
	   #             return True
	   #         r+=1
	   #     l+=1
	   # return False
	    
	    
	        
	   # arr_map={}
	   # for i , num in enumerate(arr):
	   #     complement=target-num
	   #     if complement in arr_map:
	   #         return True
	   #     arr_map[num]=1
	   # return False
	        
		# code here
		arr.sort()
		flag=False
		l=0
		r=len(arr)-1
		while l<r:
		    if arr[l]+arr[r]==target:
		        return True
		    elif arr[l]+arr[r]<target:
		        l+=1
		    else:
		        r-=1
		        
		  
		    
		    
		return False
		        