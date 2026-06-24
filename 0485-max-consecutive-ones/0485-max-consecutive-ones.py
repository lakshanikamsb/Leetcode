class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        c=0
        maximum=0
        for i in nums:
            if i==1:
                c+=1
                if c>maximum:
                    maximum=c
            else:
                c=0
        return maximum