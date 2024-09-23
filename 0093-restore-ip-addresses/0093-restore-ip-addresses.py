class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        def is_valid(segment):
            return len(segment) == 1 or (segment[0] != '0' and 0 <= int(segment) <= 255)

        def backtrack(start=0, path=[]):
            if len(path) == 4:
                if start == len(s):
                    result.append('.'.join(path))
                return

            for length in range(1, 4):
                if start + length <= len(s):
                    segment = s[start:start+length]
                    if is_valid(segment):
                        backtrack(start+length, path + [segment])

        result = []
        backtrack()
        return result