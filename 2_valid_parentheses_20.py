'''
https://leetcode.com/problems/valid-parentheses/description/
'''

# 100% result. 

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        values_dict = {
            "}": "{",
            ")": "(",
            "]": "["
        }

        for elem in s:
            
            if elem in values_dict:

                if stack and stack[-1] == values_dict[elem]:
                    stack.pop()
                    continue

            stack.append(elem)

        return not stack


print(Solution().isValid("()[]{}"))

print(Solution().isValid("(]"))