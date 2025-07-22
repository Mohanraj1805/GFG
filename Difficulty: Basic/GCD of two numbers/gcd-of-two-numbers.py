class Solution:
    def gcd(self, a, b):
        # code here
        if b==0:
            return a
        else:
            return self.gcd(b,a%b)