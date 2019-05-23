"""
    38. Count and Say
    Easy

    The count-and-say sequence is the sequence of integers with the first five terms as following:

    1.     1
    2.     11
    3.     21
    4.     1211
    5.     111221
    1 is read off as "one 1" or 11.
    11 is read off as "two 1s" or 21.
    21 is read off as "one 2, then one 1" or 1211.

    Given an integer n where 1 ≤ n ≤ 30, generate the nth term of the count-and-say sequence.

    Note: Each term of the sequence of integers will be represented as a string.

    Example 1:

    Input: 1
    Output: "1"
    Example 2:

    Input: 4
    Output: "1211"
"""


class Solution:

    def gen_next_say_string(self, say_string: str):
        def _gen_parts(say_string):
            cnt = 1
            prev_c = say_string[0]
            for c in say_string[1:]:
                if prev_c != c:
                    yield "{}{}".format(cnt, prev_c)
                    cnt = 0
                cnt += 1
                prev_c = c
            yield "{}{}".format(cnt, prev_c)

        return ''.join(_gen_parts(say_string))

    def countAndSay(self, n: int) -> str:
        say_string = "1"

        for i in range(n-1):
            say_string = self.gen_next_say_string(say_string)
        return say_string
