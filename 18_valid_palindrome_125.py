from print_and_sleep import print_and_sleep

class Solution:
    def isPalindrome(self, s: str) -> bool:
      left = 0
      right = len(s) - 1

      while left < right:

          if not s[left].isalnum():
              left += 1

          elif not s[right].isalnum():
              right -= 1

          elif s[left].lower() != s[right].lower():

              return False

          else:
              left += 1
              right -= 1

      return True


s = "A man, a plan, a canal: Panama"
print_and_sleep(f'result -> {Solution().isPalindrome(s)}')

s = "race a car"
print_and_sleep(f'result -> {Solution().isPalindrome(s)}')

s = " "
print_and_sleep(f'result -> {Solution().isPalindrome(s)}')