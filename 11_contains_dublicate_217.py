from typing import List
from time import sleep

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        frequency_set = set()

        for elem in nums:
            print(f'elem -> {elem}')
            if elem not in frequency_set:

                frequency_set.add(elem)

            else:

                return True

        return False

nums = [1,2,3,1]
print(Solution().containsDuplicate(nums=nums))


nums = [1,2,3,4]
print(Solution().containsDuplicate(nums=nums))