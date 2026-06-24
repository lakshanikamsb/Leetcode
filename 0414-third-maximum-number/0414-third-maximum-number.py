class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        elem_count=1
        prev_element=nums[0]
        for index in range(len(nums)):
            if nums[index]!=prev_element:
                elem_count+=1
                prev_element=nums[index]
            if elem_count==3:
                return nums[index]
        return nums[0]