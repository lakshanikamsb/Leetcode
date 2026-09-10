class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        stack=[]
        ans=[0]*n
        prev=0
        for log in logs:
            a=log.split(":")
            id=int(a[0])
            type=a[1]
            time=int(a[2])
            if type=="start":
                if stack:
                    ans[stack[-1]]+=time-prev
                stack.append(id)
                prev=time
            else:
                ans[stack[-1]]+=time-prev+1
                stack.pop()
                prev=time+1
        return ans