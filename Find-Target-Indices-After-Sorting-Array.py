class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        new = []
        for i in range(len(nums)):
            if nums[i] == target: new.append(i)
        return new
