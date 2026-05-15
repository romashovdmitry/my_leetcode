from time import sleep

class Solution:

    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):

            return False
        frequency = {}

        for elem in s:
            
            frequency[elem] = frequency.get(elem, 0) + 1
    
        for elem in t:

            if elem not in frequency or frequency[elem] == 0:

                return False
            frequency[elem] -= 1

        return True



print('\n')
s = "anagram"
t = "nagaram"
print(Solution().isAnagram(s=s, t=t))
print('\n')

s = "rat"
t = "car"
print(Solution().isAnagram(s=s, t=t))
print('\n')

