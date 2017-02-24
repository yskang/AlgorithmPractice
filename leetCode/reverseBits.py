class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        bin_string = str(bin(n))[2:]
        zero_padded_string = "0" * (32-len(bin_string)) + bin_string
        return int(''.join(reversed(zero_padded_string)), 2)


sol = Solution()
print(sol.reverseBits(1))