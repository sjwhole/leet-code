from typing import List


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        child_pointer = 0

        g.sort()
        s.sort()
        for cookie in s:
            if cookie >= g[child_pointer]:
                child_pointer += 1
                if child_pointer == len(g):
                    break

        return child_pointer
