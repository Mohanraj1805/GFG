class Solution:
    def thirdLargest(self,arr):
        n=len(arr)
        if n <3:
            return -1 
        fi=se=th=float('-inf')
        for i in arr:
            if i > fi:
                th=se
                se=fi
                fi=i
            elif i > se:
                th=se
                se=i
            elif i > th:
                th=i
        return th if th != float('-inf') else -1
        
        
            
        # code here
        # n=len(arr)
        # if n<3:
        #     return -1
        # fi=se= th=float('-inf')
        # for i in arr:
        #     if i > fi:
        #         th=se
        #         se=fi
        #         fi=i
        #     elif i > se:
        #         th=se
        #         se=i
        #     elif i > th:
        #         th=i
        # return th if th!=float('-inf') else -1
        