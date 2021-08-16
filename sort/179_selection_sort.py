from typing import List


class Solution:
    def compare(self, n1: int, n2: int) -> bool:
        return str(n1) + str(n2) < str(n2) + str(n1)

    def largestNumber(self, nums: List[int]) -> str:
        for i in range(1, len(nums)):
            j = i
            while j > 0 and self.compare(nums[j - 1], nums[j]):
                nums[j - 1], nums[j] = nums[j], nums[j - 1]
                j -= 1
        return str(int("".join([str(num) for num in nums])))
