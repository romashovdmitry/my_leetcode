from typing import List
from print_and_sleep import print_and_sleep

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        current_max = nums[0]
        best_sum = nums[0]

        for num in nums[1:]:
            current_max = max(num, current_max + num)
            best_sum = max(best_sum, current_max)

        return best_sum

nums = [-2,1,-3,4,-1,2,1,-5,4]
print(Solution().maxSubArray(nums))
# 6
# [4,-1,2,1]

nums = [5,4,-1,7,8]
print(Solution().maxSubArray(nums))
# 23
# [5,4,-1,7,8]

# nums = [1]
# print(Solution().maxSubArray(nums))

"""
Есть список чисел. Не сортированный.


"""