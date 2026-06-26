class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        l=0
        r=0
        c=0
        ans=0
        while (r<len(s)):
            if s[r] in "aeiou":
               c+=1
            while((r-l+1)>k):
                if s[l] in "aeiou":
                   c-=1
                l+=1
            if(r-l+1)==k:
                ans=max(ans,c)
            r+=1
        return ans