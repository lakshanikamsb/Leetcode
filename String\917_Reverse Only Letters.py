class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        letters=[]
        for ch in s:
            if ch.isalpha():
                letters.append(ch)
        letters=letters[::-1]
        result=""
        j=0
        for ch in s:
            if ch.isalpha():
                result+=letters[j]
                j+=1
            else:
                result+=ch
        return result
