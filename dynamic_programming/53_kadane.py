import sys
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = -sys.maxsize
        cur = 0
        for num in nums:
            cur = max(num, cur + num)
            ans = max(ans, cur)
        return ans
