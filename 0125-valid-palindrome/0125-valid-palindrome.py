class Solution:
    def isPalindrome(self, s: str) -> bool:
        a=""
        b=""
        for i in s:
            if i.isalnum():
                a+=i.lower()
        for i in range(len(a)-1,-1,-1):
            b+=a[i]
        if(a==b):
            return True
        return False