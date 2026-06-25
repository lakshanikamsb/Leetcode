class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        arr=[0]*26
        arr1=[0]*26
        for i in range(len(s1)):
            arr[ord(s1[i])-ord('a')]+=1
            arr1[ord(s2[i])-ord('a')]+=1
        if arr == arr1:
            return True
        for i in range(len(s1), len(s2)):
            arr1[ord(s2[i])-ord('a')]+=1
            arr1[ord(s2[i-len(s1)])-ord('a')]-=1
            if arr == arr1:
                return True
        return False