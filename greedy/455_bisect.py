from bisect import bisect_right
from typing import List


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        ans = 0
        for cookie in s:
            if ans < bisect_right(g, cookie):
                ans += 1
        return ans
