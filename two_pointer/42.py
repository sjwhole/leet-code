from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        left, right = 0, len(height) - 1
        left_pre, right_pre = height[left], height[right]

        volume = 0

        while left < right:
            if height[left] <= height[right]:
                left += 1
                left_pre = max(left_pre, height[left])
                volume += left_pre - height[left]
            else:
                right -= 1
                right_pre = max(right_pre, height[right])
                volume += right_pre - height[right]

        return volume
