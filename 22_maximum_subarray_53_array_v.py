from typing import List
from print_and_sleep import print_and_sleep

from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        
        # Для отслеживания максимальной суммы
        current_max = global_max = nums[0]
        
        # Для отслеживания текущего подмассива
        current_start = 0
        best_start = 0
        best_end = 0
        
        for i in range(1, len(nums)):
            # Если начать заново выгоднее
            if nums[i] > current_max + nums[i]:
                current_max = nums[i]
                current_start = i
            else:
                current_max = current_max + nums[i]
            
            # Если нашли лучшее решение
            if current_max > global_max:
                global_max = current_max
                best_start = current_start
                best_end = i
        
        return nums[best_start : best_end + 1]

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