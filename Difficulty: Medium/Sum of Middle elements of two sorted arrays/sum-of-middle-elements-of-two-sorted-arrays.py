#User function Template for python3

class Solution:
    def sum_of_middle_elements(self, arr1, arr2):
        # code here
        ans=[]
        i=0
        j=0
        while i <= len(arr1)-1 and j <= len(arr2)-1:
            if arr1[i]<arr2[j]:
                ans.append(arr1[i])
                i+=1
            elif arr1[i]==arr2[j]:
                ans.append(arr1[i])
                i+=1
            else:
                ans.append(arr2[j])
                j+=1
        if i < len(arr1):
            ans += arr1[i:]
        if j < len(arr2):
            ans += arr2[j:]
        n = len(ans) // 2
        return ans[n] + ans[n-1]