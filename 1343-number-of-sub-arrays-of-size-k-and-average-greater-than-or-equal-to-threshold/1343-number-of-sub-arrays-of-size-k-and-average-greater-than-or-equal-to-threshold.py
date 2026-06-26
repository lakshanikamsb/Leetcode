class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        l=0
        r=0
        c=0
        ans=0
        sum=0
        while(r<len(arr)):
            sum+=arr[r]
            if(r-l+1)==k:
                if sum//k >= threshold:
                    c+=1
                sum-=arr[l]
                l+=1
            r+=1
        return c