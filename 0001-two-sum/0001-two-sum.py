class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        num_dict = {num:i for i, num in enumerate(nums)}
        for i, num in enumerate(nums):
            if target - num in num_dict.keys():
                if num_dict[target-num] != i:
                    return [i, num_dict[target-num]]
