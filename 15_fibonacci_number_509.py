from print_and_sleep import print_and_sleep

class Solution:
    def fib(self, n: int) -> int:

        if n == 0:
            return 0
        
        elif n == 1:
            return 1

        return (
            Solution().fib(n-1) + Solution().fib(n-2)
        )


print_and_sleep(f'result -> {Solution().fib(3)}')

print_and_sleep(f'result -> {Solution().fib(5)}')