class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_len=0
        for i in accounts:
            s=0
            for x in i:
                s+=x
                max_len=max(max_len,s)
        return max_len