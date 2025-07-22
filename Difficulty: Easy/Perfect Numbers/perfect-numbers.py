class Solution:
    def isPerfect(self, n):
        # code here 
        if n <= 1:
            return False
        sum_factors = 1  # 1 is always a factor
        i = 2
       
        while i*i <n:
            if n % i == 0:
                sum_factors += i
                if i != n // i:  # Avoid adding square root twice
                    sum_factors += n // i
            i += 1
        return sum_factors == n