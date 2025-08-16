#User function Template for python3
class Solution:
	def countSubstr(self, S):
		# your code here
		count=0
		for i in S:
		    if i=='1':
		        count+=1
		return (count*(count-1))//2
		 
		      
		      
		      