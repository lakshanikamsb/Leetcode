class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        j=1
        for i in range(len(nums)):
            if(nums[i]>nums[j]):
                nums[i],nums[j]=nums[j],nums[i]
        j+=1
