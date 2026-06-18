class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        arr=[]
        arr1=[]
        a=0
        for i in range(len(s)):
            if(s[i]==c):
                arr.append(i)
        for i in range(len(s)):
            minimum=abs(arr[0]-i)
            for j in range(len(arr)):
                a=abs(arr[j]-i)
                if a<minimum:
                   minimum=a
            arr1.append(minimum)
        return arr1
