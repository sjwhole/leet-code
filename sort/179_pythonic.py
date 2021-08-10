from functools import cmp_to_key
from typing import List


class Solution:
    def compare(self, n1: int, n2: int) -> int:
        state = str(n1) + str(n2) < str(n2) + str(n1)
        if state:
            return 1
        else:
            return -1

    def largestNumber(self, nums: List[int]) -> str:
        nums.sort(key=cmp_to_key(self.compare))
        return str(int("".join([str(num) for num in nums])))
