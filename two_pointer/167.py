from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        while left < right:
            hab = numbers[left] + numbers[right]
            if hab == target:
                return [left + 1, right + 1]
            elif hab > target:
                right -= 1
            else:
                left += 1
