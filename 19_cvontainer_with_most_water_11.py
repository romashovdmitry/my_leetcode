from typing import List
from print_and_sleep import print_and_sleep

class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        left, right = 0, len(height) - 1

        while left < right:

            max_area = max(
                max_area,
                min(height[left], height[right]) * (right-left)
            )

            if height[left] <= height[right]:
                left += 1

            else:
                right -= 1

        return max_area

height = [1,8,6,2,5,4,8,3,7]
print(Solution().maxArea(height=height))