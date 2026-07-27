from typing import List

class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
    
        if not nums:

            return 0
        k = 1

        for elem_index in range(1, len(nums)):

            if nums[k-1] != nums[elem_index]:
                nums[k] = nums[elem_index]
                k += 1

        print(f'nums ->! {nums}')
        return k

nums = [1,1,2]
# nums = [0,1,0,0,0,1]
print(Solution.removeDuplicates(nums))
