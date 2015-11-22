class Solution(object):
    def minWindow(self, s, t):
        slow,fast,tmplen,minlen,result,charFreq,window=0,0,0,len(s)+1,"",{},{}
        for ch in t:
            charFreq[ch]=charFreq[ch]+1 if ch in charFreq else 1
        while fast<len(s):
            fastChar=s[fast]
            if fastChar in charFreq:
                window[fastChar]=window[fastChar]+1 if fastChar in window else 1
                if window[fastChar]<=charFreq[fastChar]: tmplen+=1
            if tmplen>=len(t):
                while s[slow] not in charFreq or window[s[slow]]>charFreq[s[slow]]:
                    if s[slow] in window: window[s[slow]]-=1
                    slow+=1
                if fast-slow+1<minlen:
                    minlen,result=fast-slow+1, s[slow:fast+1]
            fast+=1
        return result

print Solution().minWindow("ADOBECODEBANC","ABC")