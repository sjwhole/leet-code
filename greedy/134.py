from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1

        ans = 0
        fuel = 0
        for i in range(len(gas)):
            if fuel + gas[i] < cost[i]:
                ans = i + 1
                fuel = 0
            else:
                fuel += gas[i] - cost[i]
        return ans
