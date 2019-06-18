"""

67. Add Binary
Easy
"""


class Solution:

    @staticmethod
    def addTwoBits(a: str, b: str) -> str:
        """ Adds two bits together returns the str representation """
        if (a == '0') and (b == '0'):
            return '00'

        elif ((a == '1') and (b == '0')) or \
             ((a == '0') and (b == '1')):
            return '01'

        else:   # both are 1
            return '10'

    def addBinary(self, a: str, b: str) -> str:

        # make b the bigger string
        if len(b) <= len(a):
            a, b = b, a

        binary_sum = list(b)

        carry_bit = '0'
        a_length, b_length = len(a), len(b)
        rev_a, rev_b = reversed(a), reversed(b)
        for i, (c1, c2) in enumerate(zip(rev_a, rev_b)):
            ind = b_length - i - 1
            tmp_carry_bit1, bit = self.addTwoBits(c1, c2)
            tmp_carry_bit2, bit = self.addTwoBits(bit, carry_bit)

            # not possible for both bits to be '1'
            _, carry_bit = self.addTwoBits(tmp_carry_bit1, tmp_carry_bit2)
            binary_sum[ind] = bit

        for i in range(a_length, b_length):
            ind = b_length - i - 1
            if carry_bit == '0': break
            carry_bit, bit = self.addTwoBits(carry_bit, binary_sum[ind])
            binary_sum[ind] = bit

        if carry_bit == '1': binary_sum.insert(0, '1')

        return ''.join(binary_sum)


if __name__ == "__main__":
    sol = Solution()
    print(sol.addBinary('11', '1'))
