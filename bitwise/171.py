class Solution:
    def hammingWeight(self, n: int) -> int:
        return str(bin(n ^ 0)).count("1")
