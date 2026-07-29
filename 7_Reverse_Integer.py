class Solution:
    def reverse(self, x: int) -> int:
        if x >= 0:
            sign = 1
        else:
            sign = -1

        x = int(str(abs(x))[::-1]) * sign

        if -2**31 <= x <= 2**31 - 1:
            return x

        return 0
