class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l=0
        r=0
        zero=0
        Max=0
        while(r<len(nums)):
            if(nums[r]==0):
                zero+=1
            while(zero>k):
                if(nums[l]==0):
                   zero-=1
                l+=1
            Max=max(Max,r-l+1)
            r+=1
        return Max