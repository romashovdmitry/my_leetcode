'''
Two Sum: https://leetcode.com/problems/two-sum/
'''

# my solution

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        
        for index_1 in range(0, len(nums)):
            index_2_value = target - nums[index_1]

            for index_2 in range(index_1+1, len(nums)):

                if nums[index_2] == index_2_value:

                    return index_1, index_2


print(Solution().twoSum([3,3], 6))  # [0, 1]


# get from LeetCode as fastest Solution

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hashmap={}
        for i in range(len(nums)):
            complement = target-nums[i]
            if complement in hashmap:
                return [i, hashmap[complement]]
            hashmap[nums[i]] = i
        return []
    

print(Solution().twoSum([3,3], 6))  # [0, 1]

# from Gemini less thatn 2(n)
# beats 100% by speed

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        prev_map = {}  # val : index

        for i, n in enumerate(nums):
            print(f'iii -> {i}')
            print(f'nnn -> {n}')
            diff = target - n
            if diff in prev_map:
                print(f'prev_map -> {prev_map}')
                return [prev_map[diff], i]
            prev_map[n] = i
        return []
    
print(Solution().twoSum([3,3], 6))  # [0, 1]