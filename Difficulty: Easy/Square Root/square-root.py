class Solution:
    def floorSqrt(self, n): 
        l = 1
        h = n
        while l <= h:
            mid = (l + h) // 2
            if mid * mid == n:
                return mid  # Exact square root
            if mid * mid < n:
                l = mid + 1
            else:
                h = mid - 1
        return h  # Floor square root
