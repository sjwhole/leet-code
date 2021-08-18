import bisect
from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for k, v in enumerate(numbers):
            t = target - v
            idx = bisect.bisect_left(numbers, t, k + 1)
            if len(numbers) > idx and numbers[idx] == t:
                return [k + 1, idx + 1]
