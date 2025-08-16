class Solution:
    def maximumFrequency(self, s):
        # Your Code goes here
        words=s.split()
        di={}
        max_word=None
        max_freq=0
        for i in words:
            di[i]=di.get(i,0)+1
        for i in di:
            if di[i]> max_freq:
                max_freq=di[i]
                max_word=i
        return f"{max_word} {max_freq}"