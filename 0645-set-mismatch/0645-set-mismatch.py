class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        duplicate=0
        missing=0
        for i in range(len(nums)):
            if nums.count(nums[i])==2:
               duplicate=nums[i]
               break
        for i in range(1,len(nums)+1):
            if i not in nums:
                missing=i
                break
        return [duplicate, missing]