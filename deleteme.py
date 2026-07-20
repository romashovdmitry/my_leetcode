from typing import List

from print_and_sleep import print_and_sleep

class Solution:

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        word_set: set = set(wordDict)
        boolean_list: List = [False for elem in range(len(s)+1)]        
        boolean_list[0] = True
        print_and_sleep(f'boolean list > {boolean_list}')
        for i in range(len(s) + 1):
            print_and_sleep(f's[i:] -> {s[i:]}')
            for j in range(i, len(s) + 1):
                print_and_sleep(f'under string -> {s[i:j]}')
                if s[i] and s[i:j] in word_set:
                    boolean_list[i+1] = True
                    break
        print('come here')
        return boolean_list[-1]

s = "leetcode"
wordDict = ["leet","code"]

print(Solution().wordBreak(s=s, wordDict=wordDict))  # Output: True