from typing import List
from print_and_sleep import print_and_sleep

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        return_ = 0
        max_return = 0
        previous = nums[0]

        if len(nums) <= 1:

            return len(nums)

        for elem in nums:
            print(f'return max -> {max_return}')
            print(f'elem -> {elem}')
            print(f'previous -> {previous}')
            print('\n')
            if elem == previous + 1:
                return_ += 1
            
            else:
                return_ = 0

            if return_ > max_return:
                max_return = return_

            previous = elem

        return max_return

nums = [1,2,3,4,100,200]

print(Solution().longestConsecutive(nums=nums))

#nums = [1,2,6,7,8]

#print(Solution().longestConsecutive(nums=nums))

#nums = [1,2]

#print(Solution().longestConsecutive(nums=nums))




"""
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        return_ = 0
        max_return = 0 

        if len(nums) <= 1:

            return len(nums)

        for index in range(1, len(nums)):

            if nums[index] == (nums[index - 1]+1):
                return_ += 1

            else:
                print_and_sleep(f'come to else -> {nums[index]}')
                return_ = 1
                continue

            if return_ > max_return:
                max_return = return_

        return max_return
"""