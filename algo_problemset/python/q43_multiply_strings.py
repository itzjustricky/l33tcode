"""
43. Multiply strings
Medium
"""


class Solution:

    @staticmethod
    def _singleMultiply(num: str, digit_place: int, other_num: str) -> dict:
        x = int(num)

        digit_bucket = {
            i: x * int(num)
            for i, num in enumerate(reversed(other_num), digit_place)}
        return digit_bucket

    @staticmethod
    def _convertBucketToInteger(digit_bucket: dict) -> str:
        n = len(digit_bucket)

        def _generate_digits():
            decimal_carry = 0
            for i in range(n):
                x = digit_bucket[i] + decimal_carry
                yield str(x % 10)
                decimal_carry = x // 10

            if decimal_carry > 0:
                yield(str(decimal_carry))

        int_string = ""
        for digit in _generate_digits():
            int_string = digit + int_string
        return int_string

    @staticmethod
    def _combineDigitBuckets(b1: dict, b2: dict, start_index: int):
        """ Combines the digit buckets together into b1. Will return nothing,
            the numbers from b2 are added to b1.
        """
        n = max(b2.keys())
        for i in range(start_index, n+1):
            b1[i] = b1.get(i, 0) + b2.get(i, 0)

    def multiply(self, num1: str, num2: str) -> str:
        if (num1 == "0") or (num2 == "0"): return "0"

        digit_bucket = self._singleMultiply(num1[-1], 0, num2)
        for digit_place, num in enumerate(reversed(num1[:-1]), 1):
            self._combineDigitBuckets(
                digit_bucket, self._singleMultiply(num, digit_place, num2),
                start_index=digit_place)

        return self._convertBucketToInteger(digit_bucket)


if __name__ == "__main__":
    sol = Solution()
    print(sol.multiply("123", "456"))
