from typing import List

from print_and_sleep import print_and_sleep


class Solution:

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_set = set(wordDict)
        dp = [False] * (len(s) + 1)
        dp[0] = True  # пустая строка

        for i in range(1, len(s) + 1):

            for j in range(i):
                # тут буквально проверяется является ли это True
                # if dp[j] - это буквально if True или
                # if dp[j] is True
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True

                    break
        print_and_sleep(f'dp -> {dp}')                    
        return dp[len(s)]

s = "leetcode"
wordDict = ["leet","code"]

print(Solution().wordBreak(s=s, wordDict=wordDict))  # Output: True