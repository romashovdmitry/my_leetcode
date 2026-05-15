class Solution:

    def climbStairs(self, n: int) -> int:
        
        if n <= 2:

            return n

        previous = 1
        return_ = 2

        for step in range(3, n+1):
            previous, return_ = return_, previous + return_

        return return_

print(Solution().climbStairs(4))