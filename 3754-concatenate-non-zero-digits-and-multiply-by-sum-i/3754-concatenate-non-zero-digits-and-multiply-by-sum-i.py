class Solution(object):
    def sumAndMultiply(self, n):
        x = 0
        digit_sum = 0
        place = 1

        while n > 0:
            digit = n % 10

            digit_sum += digit

            if digit != 0:
                x += digit * place
                place *= 10

            n //= 10

        return x * digit_sum
        