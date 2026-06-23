class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        i=0
        s=0
        arr=[]
        while i<len(nums):
            s+=nums[i]
            arr.append(s)
            i+=1
        return(arr)