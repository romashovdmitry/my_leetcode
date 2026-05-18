from print_and_sleep import print_and_sleep

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:

        if n == 1:

            return True

        if n % 2 != 0:

            return False

        return Solution().isPowerOfTwo(n//2)

print_and_sleep(Solution().isPowerOfTwo(5))


