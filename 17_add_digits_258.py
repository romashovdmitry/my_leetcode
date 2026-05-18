class Solution:
    def addDigits(self, num: int) -> int:
        
        if num < 10:

            return num

        return Solution().addDigits(
            sum(int(digit) for digit in str(num))
        )


print(Solution().addDigits(47))
