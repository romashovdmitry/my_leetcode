'''
https://leetcode.com/problems/longest-substring-without-repeating-characters/
'''

# beats 99%

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_map = {}
        result = 0
        left = 0

        for right, char in enumerate(s):

            if char in char_map and char_map[char] >= left:
                left = char_map[char] + 1

            char_map[char] = right

            current_len = right - left + 1

            if current_len > result:
                result = current_len
        
        return result

print(Solution().lengthOfLongestSubstring("abcabcbb")) # -> 3
print(Solution().lengthOfLongestSubstring("bbbbb")) # -> 1
print(Solution().lengthOfLongestSubstring("pwwkew")) # -> 3