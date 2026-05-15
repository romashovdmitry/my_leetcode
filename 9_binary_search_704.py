from typing import List

import time

class Solution:
    def search(self, nums: List[int], target: int) -> int:

        left = 0
        right = len(nums) -1

        while right >= left:

            mid = (right + left) // 2

            if nums[mid] == target:

                return mid

            elif target > nums[mid]:

                left = mid + 1

            else:
                right = mid - 1

        return -1


nums = [-2,0,3,5,9,12,13]
target = 13
print(f'Первый кейс: {Solution().search(nums=nums, target=target)}\n\n')

nums = [-2,0,3,5,9,12,13]
target = -2
print(f'Второй кейс{Solution().search(nums=nums, target=target)}\n\n')

nums = [-2,0,3,5,9,12,13]
target = 3
print(f'Третий кейс{Solution().search(nums=nums, target=target)}\n\n')

nums = [-2,0,3,5,9,12,13]
target = 1777
print(f'Четвёртый кейс{Solution().search(nums=nums, target=target)}\n\n')

nums = [-1]
target = 13
print(f'Пятый кейс{Solution().search(nums=nums, target=target)}\n\n')

nums = [-2]
target = -2
print(f'Шестой кейс{Solution().search(nums=nums, target=target)}\n\n')