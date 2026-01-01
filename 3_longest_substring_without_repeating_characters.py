# beats 99%

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        return_ = 0

        for elem_index in range(0, len(s)):
            stack_string = []

            for letter in s[elem_index:]:
                
                if not letter in stack_string:
                    stack_string.append(letter)
            
                else:
                    break

            if len(stack_string) > return_:
                return_ = len(stack_string)

        return return_

print(Solution().lengthOfLongestSubstring("abcabcbb")) # -> 3
print(Solution().lengthOfLongestSubstring("bbbbb")) # -> 1
print(Solution().lengthOfLongestSubstring("pwwkew")) # -> 3