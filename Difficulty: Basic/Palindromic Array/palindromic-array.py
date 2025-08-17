# Your task is to complete this function
# Function should return true/false
def isPalinArray(arr):
    # Code here
    for i in arr:
        i=str(i)
        l=0
        r=len(i)-1
        while l < r:
            if i[l] !=i[r]:
                return False
            l+=1
            r-=1
    return True