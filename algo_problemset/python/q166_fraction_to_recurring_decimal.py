class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        signAdjustment = '' if self.isNonNegative(numerator, denominator) else '-'
        numerator, denominator = abs(numerator), abs(denominator)

        wholeNumber = numerator // denominator
        # note this is to track the remainder as used in long division
        remainder = numerator % denominator

        remaindersTracker = dict()
        decimalDigits, repeatingDecimals = list(), list()

        cnt = 0
        # basically do long division
        while remainder > 0:
            remainder *= 10
            # if remainder was seen before then we have a repeating decimal
            if remainder in remaindersTracker:
                # remove the repeating decimals from decimalDigits
                numRepeating = cnt - remaindersTracker[remainder]

                repeatingDecimals = decimalDigits[-numRepeating:]
                decimalDigits = decimalDigits[:-numRepeating]
                break

            remaindersTracker[remainder] = cnt
            decimalDigits.append(remainder // denominator)
            remainder = remainder % denominator

            cnt += 1

        repeatingDecimalsString = "({})".format(''.join(map(str, repeatingDecimals))) \
            if len(repeatingDecimals) > 0 else ''

        if (len(decimalDigits) == 0) and len(repeatingDecimalsString) == 0:
            return "{}{}".format(signAdjustment, wholeNumber)
        else:
            return "{}{}.{}{}".format(
                signAdjustment,
                wholeNumber,
                ''.join(map(str, decimalDigits)),
                repeatingDecimalsString)

    def isNonNegative(self, numerator: int, denominator: int) -> bool:
        if (numerator < 0) and (denominator < 0):
            return True
        elif (numerator >= 0) and (denominator >= 0):
            return True
        elif (numerator == 0):
            return True
        else:
            return False


if __name__ == "__main__":
    sol = Solution()
    print(
        sol.fractionToDecimal(0, -5)
    )
