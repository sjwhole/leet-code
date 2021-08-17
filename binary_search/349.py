import bisect
from typing import List, Set


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> set:
        ans: Set = set()

        nums2.sort()
        for num1 in nums1:
            t = bisect.bisect_left(nums2, num1)
            if len(nums2) > t and nums2[t] == num1:
                ans.add(num1)

        return ans
