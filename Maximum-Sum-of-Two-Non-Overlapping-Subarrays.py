class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        sums = [0] * (len(nums) + 1)
        for j, i in enumerate(nums): sums[j+1] = sums[j] + i
        max1 = max2 = sum = 0
        for i in range(firstLen, len(sums) - secondLen):
            max1 = max(max1, sums[i] - sums[i- firstLen])
            sum = max(sum, max1 + sums[i+secondLen] - sums[i])    
        for i in range(secondLen, len(sums) - firstLen):
            max2 = max(max2, sums[i] - sums[i- secondLen])
            sum = max(sum, max2 + sums[i + firstLen] - sums[i])
        return sum
