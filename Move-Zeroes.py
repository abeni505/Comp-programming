class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        Zero = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[Zero],nums[i] = nums[i], nums[Zero]
                Zero += 1
        return nums   
