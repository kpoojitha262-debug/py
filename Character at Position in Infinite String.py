class Solution:
    def posInfinite(self, s, pos):
        n = len(s)
        length = n
        step = 1

        # Find the required string length
        while length < pos:
            length = 2 * length + step
            step += 1

        step -= 1

        while length > n:
            prev = (length - step) // 2

            if pos > prev + step:
                pos = length - pos + 1
            elif pos > prev:
                return '$'

            length = prev
            step -= 1

        return s[pos - 1]
