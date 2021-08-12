from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        red, white, blue = 0, len(nums) - 1, len(nums) - 1

        while red <= white:
            if nums[white] < 1:
                nums[red], nums[white] = nums[white], nums[red]
                red += 1
            elif nums[white] > 1:
                nums[blue], nums[white] = nums[white], nums[blue]
                white -= 1
                blue -= 1
            else:
                white -= 1
