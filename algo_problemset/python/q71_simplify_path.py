"""

71. Simplify Path
Medium
"""


class Solution:

    @staticmethod
    def pathSeparator(path: str):
        """ Generator that separates the path into the
            directories and file-name
        """

        name_start, prev_c = 1, '/'
        for i, c in enumerate(path[1:], 1):
            if c == '/':
                if prev_c == '/': continue
                yield path[name_start:i]
            elif prev_c == '/':
                name_start = i
            prev_c = c

        if path[-1] != '/':
            yield path[name_start:]

    def simplifyPath(self, path: str) -> str:
        if path == '': return path
        assert path[0] == '/', "Passed path variable should start with '/'."

        path_stack = list()
        for name in self.pathSeparator(path):
            if name == "..":
                if len(path_stack) > 0: path_stack.pop()
            elif name == ".":
                pass
            else:
                path_stack.append(name)

        return "/" + '/'.join(path_stack)
