class Solution:
    def largest(self, arr):
        # code here
        large=0
        for i in arr:
            if i > large :
                large=i
        return large