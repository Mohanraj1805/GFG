#User function Template for python3

class Solution:
	def reverseDigits(self, n):
	    rev=0
	    while n>0:
	        rev = rev*10 + n%10
	        n=n//10
	    return rev
		# Code here
# 		ans=''
# 		for for i in range(len(str(n)):
# 		    ans+=str(n%10)
# 		    n//=10
# 		res= ans.lstrip('0')
# 		return res
