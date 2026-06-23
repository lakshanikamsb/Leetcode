class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count=0
        for i in nums:
            c=0
            while i>0:
                c+=1
                i//=10
            if c%2==0:
                count+=1
        return count