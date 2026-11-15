class Solution:
    def subsequenceSum(self, s):
        MOD = 10**9 + 7

        digit_sum = sum(int(ch) for ch in s)

        n = len(s)

        result = digit_sum * pow(2, n - 1, MOD)

        return result % MOD
