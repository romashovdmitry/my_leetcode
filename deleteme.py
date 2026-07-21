from typing import List

from print_and_sleep import print_and_sleep

class Solution:

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        word_set: set = set(wordDict)
        boolean_list = [False for _ in range(len(s)+1)]
        boolean_list[0] = True

        for i in range(1, len(s) + 1):

            for j in range(i):

                if boolean_list[j] and s[j:i] in word_set:
                    boolean_list[i] = True
                    break

        return boolean_list[-1]

s = "leetcode"
wordDict = ["leet","code"]

print(Solution().wordBreak(s=s, wordDict=wordDict))  # Output: True