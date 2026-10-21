class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1:
            return 

        pos_1 = -1
        for i in range(len(nums) - 1, 0, -1):
            if nums[i] > nums[i - 1]:
                pos_1 = i - 1
                break

        if pos_1 == -1:
            nums.reverse()
            return

        pos_2 = -1
        for i in range(len(nums) - 1, pos_1, -1):
            if nums[i] > nums[pos_1]:
                pos_2 = i
                break

        
        nums[pos_1], nums[pos_2] = nums[pos_2], nums[pos_1]
        nums[pos_1 + 1:] = nums[pos_1 + 1:][::-1]

