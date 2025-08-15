class Solution:
    def areAnagrams(self, s1, s2):
       # code here
        if len(s1)!= len(s2):
            return False
        ans={}
        for i in range(len(s1)):
            if s1[i] in ans:
                ans[s1[i]]+=1
            else:
                ans[s1[i]]=1
        for i in range(len(s2)):
            
            if s2[i] in ans:
                ans[s2[i]]-=1
                if ans[s2[i]]==0:
                    del ans[s2[i]]
            else:
                return False
        return  len(ans)==0
          