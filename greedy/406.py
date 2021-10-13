import heapq
from typing import List


class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        heap = []

        for p in people:
            heapq.heappush(heap, (-p[0], p[1]))

        ans = []
        while heap:
            p = heapq.heappop(heap)
            print(p)
            ans.insert(p[1], [-p[0], p[1]])

        return ans
