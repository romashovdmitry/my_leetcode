from typing import List

from print_and_sleep import print_and_sleep


class Solution:

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_set = set(wordDict)
        dp = [False] * (len(s) + 1)
        dp[0] = True  # пустая строка
        print_and_sleep(f'len of dp: {len(dp)}', line_break=False)
        print_and_sleep(f"Initial DP array: {dp}", line_break=False)

        for i in range(1, len(s) + 1):
#            print_and_sleep(f"Первый цикл!", line_break=False)

            for j in range(i):
                if s[j:i] == "code":
                    print_and_sleep(f"dp[{j}] = {dp[j]}, checking '{s[j:i]}'", line_break=False)

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