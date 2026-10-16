class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        '''
        i, j = 0, 0 

        while j < len(nums):
            if nums[i] == nums[j]:
                j += 1
            else:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]
                j += 1
        return i + 1 
        '''

        if not nums:
            return 0

        k = 1

        for i in range(1, len(nums)):
            if nums[i] != nums[k - 1]:
                nums[k] = nums[i]
                k += 1

        return k