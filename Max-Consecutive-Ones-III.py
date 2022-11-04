class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        start,end,maxOnes,noZeros=0,0,0,0
        for end in range(len(nums)):
            if nums[end]==0:
                noZeros+=1
            while noZeros >k:
                if nums[start]==0:
                    noZeros-=1
                start+=1
            maxOnes=max(maxOnes,end-start+1)
            
        return maxOnes
