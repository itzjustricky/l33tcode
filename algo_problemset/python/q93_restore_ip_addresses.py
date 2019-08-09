"""

93. Restore IP Addresses
Medium
"""

from typing import List


class Solution:

    def recursiveIpGenerator(self, s: str, start: int, fields_left: int) -> List[str]:

        if (start, fields_left) in self._hash_map:
            return self._hash_map[(start, fields_left)]

        N = len(s)

        sub_ips = list()
        if fields_left == 1:
            # field_length = N - start
            bit_field = s[start:]

            # too many numbers left over
            if len(bit_field) > 3:
                pass
            # invalid bit field
            elif (len(bit_field) > 1) and bit_field.startswith('0'):
                pass
            # larger than the largest possible bit-field size
            elif bit_field.rjust(3, '0') > '255':
                pass
            else:
                sub_ips = [s[start:]]

            self._hash_map[(start, fields_left)] = sub_ips
            return sub_ips

        # ip bit-field can at most extend 3 numbers
        for end in range(start+1, min(start+4, N)):

            bit_field = s[start:end]
            if bit_field.rjust(3, '0') > '255': break

            # invalid bit field
            if (len(bit_field) > 1) and bit_field.startswith('0'):
                continue

            sub_ips.extend(
                '.'.join((bit_field, generated_ips))
                for generated_ips in self.recursiveIpGenerator(s, end, fields_left-1))

        self._hash_map[(start, fields_left)] = sub_ips
        return sub_ips

    def restoreIpAddresses(self, s: str) -> List[str]:
        # map from (start, parts-left) => <list of parts>
        self._hash_map = dict()
        return self.recursiveIpGenerator(s, 0, 4)


if __name__ == "__main__":
    from pprint import pprint

    sol = Solution()
    pprint(sol.restoreIpAddresses("25525511135"))
