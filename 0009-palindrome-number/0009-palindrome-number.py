class Solution:
    def isPalindrome(self, x: int) -> bool:
        rem=0
        rev=0
        sum=0
        nums=x
        while(x>0):
            rem=x%10
            sum=rem+(rev*10)
            rev=sum
            x//=10
        if(nums==rev):
            return True
        else:
            return False