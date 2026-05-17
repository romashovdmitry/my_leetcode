"""
    https://leetcode.com/problems/reverse-string/description/
"""
from typing import List
from time import sleep

def print_and_sleep(any_s):
    print('\n')
    print(any_s)
    sleep(1)

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """

        def helper(start, finish):

            if start > finish:

                return

            s[start], s[finish] = s[finish], s[start]

            helper(start+1, finish-1)

        helper(0, len(s) - 1)

s = ["h","e","l","l","o"]
# print(Solution().reverseString())
# в оригинале надо in place это сделать
print(Solution().reverseString(s))
