class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        a=""
        for i in s:
            if i.isalnum():
                a+=i
        b=a[::-1]
        return a==b
