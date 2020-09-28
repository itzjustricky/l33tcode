import string


class Solution:

    def convertToTitle(self, n: int) -> str:
        # the title is basically base 26 but with a lack of '0'
        # in use for excel column titles
        # Think of it as remap 'Z' -> 0 with a carry over to the next base 26 bit
        base, remainder = 26, n

        title = ''
        while remainder > 0:
            mod = remainder % 26

            if mod == 0:
                # remove the carry over from the next base 26 bit
                remainder -= 1

            title += string.ascii_uppercase[mod-1]
            remainder //= base

        return title[::-1]


if __name__ == "__main__":
    sol = Solution()
    print(
        sol.convertToTitle(701)
    )
